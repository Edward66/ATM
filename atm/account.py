import os
import json
from settings.settings import BASE_DIR
from utils import logger_info
from utils import load_file


def account_info():
    while True:
        username = input('请输入要查看的用户名,按q返回上一层').strip()
        if username.lower() == 'q':
            break
        user_info = load_file.read_db(username)
        if user_info is None:
            print('\033[31m用户名不存在\033[0m')
            return None
        print('用户\033[31m{0}的额度为{1}\033[0m'.format(username, user_info[username]['amount']))


def add_account():
    while True:
        new_username = input('请输入用户名,按q返回上一层:').strip()
        if new_username.lower() == 'q':
            break
        user_info = load_file.read_db(new_username)
        if user_info is not None or len(new_username) < 6:
            print('\033[31m用户名已存在或用户名小于6位\033[0m')
            continue
        new_username2 = input('请再次输入用户名:').strip()
        if new_username2.lower() == 'q':
            break
        if new_username == new_username2:
            password = input('请输入密码:').strip()
            password2 = input('请再次输入密码:').strip()
            if password == password2:
                new_user_info = {}
                print('正在创建战账户......')
                new_user_info[new_username] = {'username': new_username, 'password': password, 'amount': 15000, 'status': 0}
                status = load_file.write_db(new_user_info, new_username)
                if status is False:
                    print('写入数据库时出错，请稍后再试')
                    return None
                print('\033[31m创建成功\033[0m')
                logger = logger_info.logger_atm_login('add_account')
                logger.info('管理员创建了新账户,账户名为:%s' % new_username)
                break
            else:
                print('\033[31m密码不一致，请重新输入\033[0m')
        else:
            print('\033[31m用户名输入不一致，请重新输入\033[0m')


def frozen_account():
    while True:
        frozen_username = input('\033[31m请输入要冻结的账户名,按q返回上一层\033[0m').strip()
        if frozen_username.lower() == 'q':
            break
        user_info = load_file.read_db(frozen_username)
        if user_info is None:
            print('\033[31m用户名不存在\033[0m')
            return None
        user_info[frozen_username]['status'] = 1
        status = load_file.write_db(user_info, frozen_username)
        if status is False:
            print('写入数据库时出错，请稍后再试')
            return None
        logger = logger_info.logger_atm_login('frozen_account')
        logger.warning('管理员%s冻结了账户' % frozen_username)
        print('\033[31m冻结成功。\033[0m')


def manage_account(username):
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
            add_account()
        elif choice == '3':
            frozen_account()
        elif choice == '4':
            break
        else:
            print('\033[31m输入不合法，请按提示输入数字\033[0m')
