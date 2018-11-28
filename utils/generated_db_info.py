import os
import sys
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(sys)

user_info = {'edward': {'username': 'edward', 'password': '112233', 'amount': 20000, 'status': 0},
             'john': {'username': 'john', 'password': '123123', 'amount': 20000, 'status': 0},
             'mark': {'username': 'mark', 'password': '121212', 'amount': 20000, 'status': 0},
             }

goods = [{'name': '大宝SOD蜜', 'price': 10}, {'name': '洗面奶', 'price': 50}, {'name': '老面包', 'price': 15},
         {'name': '小米电视', 'price': 4000},
         {'name': '冰箱', 'price': 3000}, {'name': '海尔洗衣机', 'price': 4000},
         {'name': 'macbook air', 'price': 10000}, {'name': 'thinkpad', 'price': 8000},
         {'name': 'iphoneXS', 'price': 12000}, {'name': '老男孩教育', 'price': 13000}]

with open(os.path.join(BASE_DIR, 'db/user_info.json'), 'w', encoding='utf-8') as f:
    json.dump(user_info, f)

with open(os.path.join(BASE_DIR, 'db/goods_info.json'), 'w', encoding='utf-8') as f2:
    json.dump(goods, f2)