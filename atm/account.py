import os
import json
from settings.settings import BASE_DIR
from utils import logging_atm


def account_info(user_money):
    try:
        with open(os.path.join(BASE_DIR, 'db/user_info.json'), 'r', encoding='utf-8') as f:
            user_info = json.load(f)
    except FileNotFoundError:
        print('数据库出错或数据不存在，请稍后再试,check_account')
    else:
        print('\033[31m您的当前余额为%s\033[0m' % user_money)


def add_account(username):
    try:
        with open(os.path.join(BASE_DIR, 'db/user_info.json'), 'r', encoding='utf-8') as f:
            user_info = json.load(f)
    except:
        print('数据库出错或数据不存在，请稍后再试,add_account')
    else:
        while True:
            new_username = input('请输入用户名,按q返回上一层:').strip()
            if new_username in user_info:
                print('用户名已存在')
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
                    print('密码不一致，请重新输入')
            else:
                print('用户名输入不一致，请重新输入')


def frozen_account(username):
    try:
        with open(os.path.join(BASE_DIR, 'db/user_info.json'), 'r', encoding='utf-8') as f:
            user_info = json.load(f)
    except FileNotFoundError:
        print('数据库出错或数据不存在，请稍后再试,frozen_account')
    else:
        while True:
            choice = input('确认要冻结账户吗？确认请按y,返回上一层请按q').strip()
            if choice.lower() == 'q':
                break
            if choice.lower() == 'y':
                user_info[username]['status'] = 1
                with open(os.path.join(BASE_DIR, 'db/user_info.json'), 'w', encoding='utf-8') as f:
                    json.dump(user_info, f)
                logging_atm.logging_frozen_account(username)
                exit('冻结成功，程序自动退出。')


def manage_account(username, user_money):
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
            account_info(user_money)
        elif choice == '2':
            add_account(username)
        elif choice == '3':
            frozen_account(username)
        elif choice == '4':
            break
        else:
            print('输入不合法，请按提示输入数字')
