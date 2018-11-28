import os
import json
from settings.settings import BASE_DIR
from utils import logging_atm


def withdraw_money(username, user_money):
    try:
        with open(os.path.join(BASE_DIR, 'db/user_info.json'), 'r', encoding='utf-8') as f:
            user_info = json.load(f)
    except FileNotFoundError:
        print('\033[31m数据库出错或数据不存在，请稍后再试,withdraw\033[0m')
    else:
        while True:
            print('---------- 您当前的位置是:提现中心 ----------')
            money_take = input('请输入要提现的额度(手续费%5),返回上一层请按q:').strip()
            if money_take.isdigit():
                money_take = int(money_take)
                if user_money > (1.05 * money_take):
                    user_money = user_money - (1.05 * money_take)
                    user_info[username]['amount'] = user_money
                    with open(os.path.join(BASE_DIR, 'db/user_info.json'), 'w', encoding='utf-8') as f2:
                        json.dump(user_info, f2)
                    print('正在操作中......')
                    print('\033[31m提现成功，提现{0},手续费{1},您的当前余额为{2},继续提现请输入金额，返回上一层请按q\033[0m'.format(money_take,
                                                                                                  money_take * 0.05,
                                                                                                  user_money))
                    logging_atm.logging_withdraw(username, money_take, user_money)
                else:
                    print('\033[31m您的账户余额不足\033[0m')
            elif money_take.lower() == 'q':
                break
            else:
                print('\033[31m输入不合法，请输入数字\033[0m')
