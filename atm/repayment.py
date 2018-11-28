import os
import json
from settings.settings import BASE_DIR
from utils import logging_atm


def repayment_money(username, user_money):
    try:
        with open(os.path.join(BASE_DIR, 'db/user_info.json'), 'r', encoding='utf-8') as f:
            user_info = json.load(f)
    except FileNotFoundError:
        print('\033[31m数据库出错或数据不存在,请稍后再试,repayment\033[0m')
    else:
        while True:
            print('---------- 您当前的位置是:还款中心 ----------')
            repay_amount = input('请输入\033[31m还款金额\033[0m,返回上一层请按q').strip()
            if repay_amount.lower() == 'q':
                break
            if repay_amount.isdigit():
                repay_amount = int(repay_amount)
                user_money += repay_amount
                user_info[username]['amount'] = user_money
                print('正在还款中......')
                with open(os.path.join(BASE_DIR, 'db/user_info.json'), 'w', encoding='utf-8') as f:
                    json.dump(user_info, f)
                print('\033[31m还款成功，还款%s,您在账户余额为%s\033[0m' % (repay_amount, user_money))
                logging_atm.logging_repayment(username, repay_amount, user_money)

            else:
                print('\033[31m输入不合法，请重新输入\033[0m')
