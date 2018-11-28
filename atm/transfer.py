import os
import json
from settings.settings import BASE_DIR
from utils import logging_atm


# FileNotFoundError
def transfer_money(username, user_money):
    try:
        with open(os.path.join(BASE_DIR, 'db/user_info.json'), 'r', encoding='utf-8') as f:
            user_info = json.load(f)
    except FileNotFoundError:
        print('数据库出错或数据不存在，请稍后再试,transfer')
    else:
        while True:
            print('---------- 您当前的位置是:转账中心 ----------')
            target_username = input('请输入\033[31m要转账的用户名\033[0m,返回上一层请按q').strip()
            if target_username.lower() == 'q':
                break
            if target_username in user_info:
                while True:
                    print('---------- 您当前的位置是:转账中心 ----------')
                    transfer_amount = input('请输入\033[31m要转入的金额\033[0m，返回上一层请按q').strip()
                    if transfer_amount.lower() == 'q':
                        break
                    if transfer_amount.isdigit():
                        transfer_amount = int(transfer_amount)
                        if user_money > transfer_amount:
                            user_money -= transfer_amount
                            user_info[username]['amount'] = user_money
                            user_info[target_username]['amount'] += transfer_amount
                            print('正在转账中......')
                            with open(os.path.join(BASE_DIR, 'db/user_info.json'), 'w', encoding='utf-8') as f2:
                                json.dump(user_info, f2)
                            print('\033[31m转账成功，您向%s转账%s元,您当前的账户余额为%s\033[0m' % (target_username, transfer_amount,
                                                                                 user_money))
                            logging_atm.logging_transfer(username, target_username, transfer_amount, user_money)

                        else:
                            print('您的账户余额不足')
                    else:
                        print('输入不合法,请重新输入')
            else:
                print('用户名不存在')
