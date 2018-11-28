import os
import json

from settings.settings import BASE_DIR
from atm import credit_card


def shopping_car():
    try:
        with open(os.path.join(BASE_DIR, 'db/goods_info.json'), 'r', encoding='utf-8') as f:
            goods_info = json.load(f)
    except FileNotFoundError:
        print('\033[31m数据库出错或数据不存在，请稍后再试,shopping\033[0m')
    else:
        shopping_list = []
        while True:
            print('---------- 商品列表 ----------')
            for index, key in enumerate(goods_info):
                print(index + 1, key['name'], key['price'])
            choice = input('请选择您要购买的商品序号,按q返回上一层,按c进入结算中心').strip()
            if choice.isdigit() and int(choice) <= len(goods_info):
                print(len(goods_info))
                choice = int(choice) - 1
                shopping_list.append(goods_info[choice])
                print('------>', shopping_list)
                print('商品添加成功')
                print('你的购物车如下:')
                for index, good in enumerate(shopping_list):
                    print('\033[31m {index} {name} {price} \033[0m'.format(index=index + 1, name=good['name'],
                                                                           price=good['price']))

            elif choice.lower() == 'c':
                if shopping_list == []:
                    print('\033[31m您的购物车没有商品\033[0m')
                else:
                    print('正在进入结算中心......')
                    return credit_card.check_out(shopping_list)
            elif choice.lower() == 'q':
                print('谢谢光临，退出商城')
                break
            else:
                print('\033[31m 输入不合法，请输入正确的商品编号\033[0m')
