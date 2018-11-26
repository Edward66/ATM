# 记录每月流水
import os
import time
import logging
from logging import handlers
from settings.settings import BASE_DIR


def per_month_consume(username, money, *args, **kwargs):
    goods = args
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    fh = handlers.TimedRotatingFileHandler(filename=os.path.join(BASE_DIR, 'log/user_consume.log'), when='D',
                                           interval=30)
    fh.setLevel(logging.DEBUG)

    file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    fh.setFormatter(file_formatter)

    logger.addHandler(fh)

    goods_name = []
    for key in goods:
        goods_name.append(key['name'])
    goods_name = ','.join(goods_name)
    logger.info('用户{username}购买了:{goods},总共花费{money}元'.format(username=username, goods=goods_name, money=money))
