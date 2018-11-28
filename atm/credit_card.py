import os
import json
from utils import user_verify
from utils import logging_consume
from settings.settings import BASE_DIR


@user_verify.user_verify
def check_out(username, user_money, goods):
    if username == 'root':
        print('\033[31m 您是管理员，不能购物\033[0m')
        return None
    print('您购买的商品如下:')
    goods_price = 0
    for index, good in enumerate(goods):
        goods_price += good['price']
        print('\033[31m {index} {name} {price} \033[0m'.format(index=index + 1, name=good['name'],
                                                               price=good['price']))
    choice = input('确认购买请按任意键,退出请按q').strip()
    if choice.lower() == 'q':
        print('\033[31m欢饮下次光临\033[0m')
        return None
    else:
        user_money -= goods_price
        if user_money < -15000:
            print('\033[31m 超出额度，消费后额度为%s,您的信用额度为-15000元\033[0m' % user_money)
            return None
        try:
            with open(os.path.join(BASE_DIR, 'db/user_info.json'), 'r', encoding='utf-8') as f:
                user_info = json.load(f)
        except FileNotFoundError:
            print('\033[31m数据库出错或数据不存在，请稍后再试,credit_card\033[0m')
        else:
            user_info[username]['amount'] = user_money
            with open(os.path.join(BASE_DIR, 'db/user_info.json'), 'w', encoding='utf-8') as f2:
                json.dump(user_info, f2)
            print('购买成功,您的账户余额为%s' % user_money)
            logging_consume.per_month_consume(username, goods_price, *goods)
