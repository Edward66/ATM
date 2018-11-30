import os
import json
from utils import user_verify
from utils import logger_info
from settings.settings import BASE_DIR
from utils import load_file


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
        user_info = load_file.read_db(username)
        if user_info is None:
            print('\033[31m数据库出错或数据不存在，请稍后再试\033[0m')
            return None
        user_info[username]['amount'] = user_money
        status = load_file.write_db(user_info, username)
        if status is False:
            print('写入数据库时出错，请稍后再试')
            return None
        print('购买成功,您的账户余额为%s' % user_money)
        logger_info.per_month_consume(username, goods_price, *goods)
