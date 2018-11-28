import os
import json
from settings.settings import BASE_DIR
from utils import logging_atm


def account_info():
    try:
        with open(os.path.join(BASE_DIR, 'db/user_info.json'), 'r', encoding='utf-8') as f:
            user_info = json.load(f)
    except FileNotFoundError:
        print('\033[31m数据库出错或数据不存在，请稍后再试,check_account\033[0m')
    else:
        while True:
            username = input('请输入要查看的用户名,按q返回上一层').strip()
            if username in user_info:
                print('用户\033[31m{0}的额度为{1}\033[0m'.format(username, user_info[username]['amount']))
            elif username.lower() == 'q':
                break
            else:
                print('\033[31m用户名不存在\033[0m')


def add_account(username):
    try:
        with open(os.path.join(BASE_DIR, 'db/user_info.json'), 'r', encoding='utf-8') as f:
            user_info = json.load(f)
    except:
        print('\033[31m数据库出错或数据不存在，请稍后再试,add_account\033[0m')
    else:
        while True:
            new_username = input('请输入用户名,按q返回上一层:').strip()
            if new_username in user_info or len(new_username) < 6:
                print('\033[31m用户名已存在或用户名小于6位\033[0m')
                continue
            if new_username.lower() == 'q':
                break
            new_username2 = input('请再次输入用户名:').strip()
            if new_username2.lower() == 'q':
                break
            if new_username == new_username2:
                password = input('请输入密码:').strip()
                password2 = input('请再次输入密码:').strip()
                if password == password2:
                    print('正在创建战账户......')
                    user_info[new_username] = {'username': new_username, 'password': password, 'amount': 0, 'status': 0}
                    with open(os.path.join(BASE_DIR, 'db/user_info.json'), 'w', encoding='utf-8') as f:
                        json.dump(user_info, f)
                    print('\033[31m创建成功\033[0m')
                    logging_atm.logging_add_account(username, new_username)
                    break
                else:
                    print('\033[31m密码不一致，请重新输入\033[0m')
            else:
                print('\033[31m用户名输入不一致，请重新输入\033[0m')


def frozen_account(username):
    try:
        with open(os.path.join(BASE_DIR, 'db/user_info.json'), 'r', encoding='utf-8') as f:
            user_info = json.load(f)
    except FileNotFoundError:
        print('\033[31m数据库出错或数据不存在，请稍后再试,frozen_account\033[0m')
    else:
        while True:
            frozen_username = input('\033[31m请输入要冻结的账户名,按q返回上一层\033[0m').strip()
            if frozen_username.lower() == 'q':
                break
            if frozen_username in user_info:
                user_info[frozen_username]['status'] = 1
                with open(os.path.join(BASE_DIR, 'db/user_info.json'), 'w', encoding='utf-8') as f:
                    json.dump(user_info, f)
                logging_atm.logging_frozen_account(username)
                print('\033[31m冻结成功。\033[0m')
            else:
                print('\033[31m用户名不存在，请重新输入\033[0m')


def manage_account(username, user_money):
    if username != 'root':
        print('\033[31m非root用户不能管理账户\033[0m')
        return None
    info = '''
    ---------- 欢迎来到账户管理中心 ----------
    请选择要进行的操作:
    1.查看用户额度
    2.添加账户
    3.冻结账户
    4.返回上一层
    '''
    while True:
        print(info)
        choice = input('>>>').strip()
        if choice == '1':
            account_info()
        elif choice == '2':
            add_account(username)
        elif choice == '3':
            frozen_account(username)
        elif choice == '4':
            break
        else:
            print('\033[31m输入不合法，请按提示输入数字\033[0m')
