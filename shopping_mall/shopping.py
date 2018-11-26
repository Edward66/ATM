import os
import json

from settings.settings import BASE_DIR
from atm import credit_card


def shopping_car():
    with open(os.path.join(BASE_DIR, 'db/goods_info.json'), 'r', encoding='utf-8') as f:
        goods_info = json.load(f)
    shopping_list = []
    while True:
        print('---------- 商品列表 ----------')
        for index, key in enumerate(goods_info):
            print(index + 1, key['name'], key['price'])
        choice = input('请选择您要购买的商品序号,按q退出').strip()
        if choice.lower() == 'q':
            if shopping_list == []:
                print('退出商城')
                break
            else:
                print('您在购物车有商品')
                print('正在进入结算中心......')
                return credit_card.check_out(shopping_list)
        if choice.isdigit() and len(choice) <= len(goods_info):
            choice = int(choice) - 1
            shopping_list.append(goods_info[choice])
            print('------>', shopping_list)
            print('商品添加成功')
            print('你的购物车如下:')
            for index, good in enumerate(shopping_list):
                print('\033[31m {index} {name} {price} \033[0m'.format(index=index + 1, name=good['name'],
                                                                       price=good['price']))
            choice2 = input('继续购买请按任意键，结算请按c').strip()
            while True:
                if choice2.lower() == 'c':
                    print('正在进入结算中心......')
                    return credit_card.check_out(shopping_list)
                else:
                    break
        else:
            print('输入不合法，请输入商品编号')
