import os
import json
from utils import user_verify
from utils import logging_consume
from settings.settings import BASE_DIR


@user_verify.user_verify
def check_out(username, user_amount, goods):
    print('您购买的商品如下:')
    goods_price = 0
    for index, good in enumerate(goods):
        goods_price += good['price']
        print('\033[31m {index} {name} {price} \033[0m'.format(index=index + 1, name=good['name'],
                                                               price=good['price']))
    choice = input('确认购买请按任意键,退出请按q').strip()
    if choice.lower() == 'q':
        print('欢饮下次光临')
        return None
    else:
        user_amount -= goods_price
        with open(os.path.join(BASE_DIR, 'db/user_info.json'), 'r', encoding='utf-8') as f:
            user_info = json.load(f)
        user_info[username]['amount'] = user_amount
        with open(os.path.join(BASE_DIR, 'db/user_info.json'), 'w', encoding='utf-8') as f2:
            json.dump(user_info, f2)
        print('购买成功')
        logging_consume.per_month_consume(username, goods_price, *goods)
