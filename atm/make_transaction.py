import os
import json
from settings.settings import BASE_DIR, INTEREST
from utils import logger_info
from utils import load_file


def withdraw_money(username, user_money):
    user_info = load_file.read_db(username)
    if user_info is None:
        print('\033[31m数据库出错或数据不存在，请稍后再试\033[0m')
        return None
    while True:
        print('---------- 您当前的位置是:提现中心 ----------')
        money_take = input('请输入要提现的额度(手续费%5),返回上一层请按q:').strip()
        if money_take.isdigit():
            money_take = float(money_take)
            if user_money > (INTEREST['withdraw'] * money_take):
                user_money -= (INTEREST['withdraw'] * money_take)
                user_info[username]['amount'] = user_money
                status = load_file.write_db(user_info, username)
                if status is False:
                    print('写入数据库时出错，请稍后再试')
                    return None
                print('正在操作中......')
                print('\033[31m提现成功，提现{0},手续费{1},您的当前余额为{2},继续提现请输入金额，返回上一层请按q\033[0m'.format(money_take,
                                                                                              money_take * INTEREST[
                                                                                                  'withdraw'],
                                                                                              user_money))
                logger = logger_info.logger_atm_login('withdraw')
                logger.info('用户{0}取款,手续费{1},当前余额为{2}'.format(username, money_take * INTEREST['withdraw'], user_money))
            else:
                print('\033[31m您的账户余额不足\033[0m')
        elif money_take.lower() == 'q':
            break
        else:
            print('\033[31m输入不合法，请输入数字\033[0m')


def transfer_money(username, user_money):
    user_info = load_file.read_db(username)
    if user_info is None:
        print('\033[31m数据库出错或数据不存在，请稍后再试\033[0m')
        return None
    while True:
        print('---------- 您当前的位置是:转账中心 ----------')
        target_username = input('请输入\033[31m要转账的用户名\033[0m,返回上一层请按q').strip()
        if target_username.lower() == 'q':
            break
        if target_username == username:
            print('\033[31m您不能转账给自己\033[0m')
            continue
        target_user_info = load_file.read_db(target_username)
        if target_user_info is None:
            print('用户名不存在')
        while True:
            print('---------- 您当前的位置是:转账中心 ----------')
            transfer_amount = input('请输入\033[31m要转入的金额\033[0m，返回上一层请按q').strip()
            if transfer_amount.lower() == 'q':
                break
            if transfer_amount.isdigit():
                transfer_amount = float(transfer_amount)
                if user_money > transfer_amount:
                    user_money -= transfer_amount
                    user_info[username]['amount'] = user_money
                    target_user_info[target_username]['amount'] += transfer_amount
                    print('正在转账中......')
                    status = load_file.write_db(user_info, username)
                    if status is False:
                        print('向%s写入数据库时出错，请稍后再试' % username)
                        return None
                    target_status = load_file.write_db(target_user_info, target_username)
                    if target_status is False:
                        print('向%s写入数据库时出错，请稍后再试' % target_username)
                        return None
                    print('\033[31m转账成功，您向%s转账%s元,您当前的账户余额为%s\033[0m' % (target_username, transfer_amount,
                                                                         user_money))

                    logger = logger_info.logger_atm_login('transfer')

                    logger.info('用户{0}向用户{1}转账{2}元,账户余额还剩{3}'.format(username, target_username, transfer_amount,
                                                                     user_money))

                else:
                    print('\033[31m您的账户余额不足\033[0m')
            else:
                print('\033[31m输入不合法,请重新输入\033[0m')


def repayment_money(username, user_money):
    user_info = load_file.read_db(username)
    if user_info is None:
        print('\033[31m数据库出错或数据不存在，请稍后再试\033[0m')
        return None
    while True:
        print('---------- 您当前的位置是:还款中心 ----------')
        repay_amount = input('请输入\033[31m还款金额\033[0m,返回上一层请按q').strip()
        if repay_amount.lower() == 'q':
            break
        if repay_amount.isdigit():
            repay_amount = float(repay_amount)
            user_money += repay_amount
            user_info[username]['amount'] = user_money
            print('正在还款中......')
            status = load_file.write_db(user_info, username)
            if status is False:
                print('写入数据库时出错，请稍后再试')
                return None
            print('\033[31m还款成功，还款%s,您在账户余额为%s\033[0m' % (repay_amount, user_money))
            logger = logger_info.logger_atm_login('repayment')
            logger.info('用户{0}还款{1}元账户余额为{2}元'.format(username, repay_amount, user_money))

        else:
            print('\033[31m输入不合法，请重新输入\033[0m')
