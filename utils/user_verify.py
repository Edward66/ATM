import os
import json
from settings.settings import BASE_DIR


def user_verify(func):
    def wrapper(*args, **kwargs):
        try:
            with open(os.path.join(BASE_DIR, 'db/user_info.json'), 'r', encoding='utf-8') as f:
                user_info = json.load(f)
        except:
            print('数据库出错或数据不存在，请稍后再试,user_verify')
        else:
            count = 3
            while True:
                count -= 1
                print('请先登录,按q退出')
                username = input('username:').strip()
                if username.lower() == 'q':
                    break
                if username in user_info:
                    if user_info[username]['status'] == 1:
                        print('账号已被冻结')
                        break
                    password = input('password:').strip()
                    if password.lower() == 'q':
                        break
                    if username == user_info[username]['username'] and password == user_info[username]['password']:
                        print('登录成功')
                        user_money = user_info[username]['amount']
                        return func(username, user_money, *args, **kwargs)
                    else:
                        if count == 0:
                            user_info[username]['status'] = 1
                            with open(os.path.join(BASE_DIR, 'db/user_info.json'), 'w', encoding='utf-8') as f2:
                                json.dump(user_info, f2)
                            print('登录失败三次，自动退出')
                            break
                        else:
                            print('密码错误，请重新输入')
                else:
                    print('用户名不存在')

    return wrapper
