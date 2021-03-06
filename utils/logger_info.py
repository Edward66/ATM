import os
import logging
from logging import handlers
from settings.settings import BASE_DIR
from settings.settings import BASE_LOG


def per_month_consume(username, money, *args, **kwargs):
    goods = args
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    fh = handlers.TimedRotatingFileHandler(filename=os.path.join(BASE_DIR, 'log/%s_consume.log' % username),
                                           when='D',
                                           interval=30)
    fh.setLevel(logging.DEBUG)

    file_formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(message)s')
    fh.setFormatter(file_formatter)

    logger.addHandler(fh)

    goods_name = []
    for key in goods:
        goods_name.append(key['name'])
    goods_name = ','.join(goods_name)
    logger.info('您购买了:{goods},总共花费{money}元'.format(goods=goods_name, money=money))


def logger_atm_login(log_type):
    logger = logging.getLogger(log_type)
    logger.setLevel(logging.DEBUG)

    fh = handlers.RotatingFileHandler(filename=os.path.join(BASE_LOG, '%s_log' % log_type), maxBytes=1024 * 1024,
                                      backupCount=100)
    fh.setLevel(logging.DEBUG)

    file_formater = logging.Formatter('%(asctime)s : %(name)s : %(levelname)s : %(message)s')
    fh.setFormatter(file_formater)

    logger.addHandler(fh)

    return logger
