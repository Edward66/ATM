import os
import json
from settings.settings import BASE_DIR
from utils import logger_info
from utils import load_file


def user_verify(func):
    def wrapper(*args, **kwargs):
        count = 3
        while True:
            count -= 1
            print('请先登录,按q退出')
            username = input('username:').strip()
            if username.lower() == 'q':
                break
            user_info = load_file.read_db(username)
            if user_info is None:
                print('用户名不存在')
                break

            if user_info[username]['status'] == 1:
                exit('账号已被冻结')
            password = input('password:').strip()
            if password.lower() == 'q':
                break
            if username == user_info[username]['username'] and password == user_info[username]['password']:
                print('登录成功')
                user_money = user_info[username]['amount']
                logger = logger_info.logger_atm_login('login')
                logger.info('用户%s登陆成功' % username)
                return func(username, user_money, *args, **kwargs)
            else:
                if count == 0:
                    exit('登录失败三次，自动退出')
                else:
                    print('\033[31m密码错误，请重新输入\033[0m')

    return wrapper
