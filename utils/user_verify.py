import os
import json
from settings.settings import BASE_DIR


def user_verify(func):
    def wrapper(*args, **kwargs):
        with open(os.path.join(BASE_DIR, 'db/user_info.json'), 'r', encoding='utf-8') as f:
            user_info = json.load(f)
        count = 3
        while True:
            count -= 1
            print('请先登录,按q退出')
            username = input('username:').strip()
            if username.lower() == 'q':
                break
            if username in user_info:
                if user_info[username]['status'] == 1:
                    print('用户已被锁定')
                    break
                password = input('password:').strip()
                if password.lower() == 'q':
                    break
                if username == user_info[username]['username'] and password == user_info[username]['password']:
                    print('登录成功')
                    user_amount = user_info[username]['amount']
                    return func(username, user_amount, *args, **kwargs)
                else:
                    if count == 0:
                        user_info[username]['status'] = 1
                        with open(os.path.join(BASE_DIR, 'db/user_info.json'), 'r', encoding='utf-8') as f2:
                            json.dump(user_info, f2)
                        print('登录失败三次，自动退出')
                        break
                    else:
                        print('密码错误，请重新输入')
            else:
                print('用户名不存在')

    return wrapper
