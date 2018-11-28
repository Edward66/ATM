import os
import logging
from logging import handlers
from settings.settings import BASE_DIR


def logging_withdraw(username, money_take, user_money):
    logger = logging.getLogger('withdraw')
    logger.setLevel(logging.DEBUG)

    fh = handlers.RotatingFileHandler(
        filename=os.path.join(BASE_DIR, 'log/%s_withdraw.log' % username), maxBytes=1024 * 1024, backupCount=100)
    fh.setLevel(logging.DEBUG)

    file_formater = logging.Formatter('%(asctime)s : %(name)s : %(levelname)s : %(message)s')
    fh.setFormatter(file_formater)

    logger.addHandler(fh)

    logger.info('用户{0}提现{1}元,手续费{2}元,账户余额还剩{3}元'.format(username, money_take, money_take * 0.05, user_money))


def logging_transfer(username, targer_username, transfer_amount, user_money):
    logger = logging.getLogger('transfer')
    logger.setLevel(logging.DEBUG)

    fh = handlers.RotatingFileHandler(
        filename=os.path.join(BASE_DIR, 'log/%s_transfer.log' % username), maxBytes=1024 * 1024, backupCount=100)
    fh.setLevel(logging.DEBUG)

    file_formater = logging.Formatter('%(asctime)s : %(name)s : %(levelname)s : %(message)s')
    fh.setFormatter(file_formater)

    logger.addHandler(fh)

    logger.info('用户{0}向用户{1}转账{2}元,账户余额还剩{3}'.format(username, targer_username, transfer_amount, user_money))


def logging_repayment(username, repay_amount, user_money):
    logger = logging.getLogger('repayment')
    logger.setLevel(logging.DEBUG)

    fh = handlers.RotatingFileHandler(
        filename=os.path.join(BASE_DIR, 'log/%s_repayment.log' % username), maxBytes=1024 * 1024, backupCount=100)
    fh.setLevel(logging.DEBUG)

    file_formater = logging.Formatter('%(asctime)s : %(name)s : %(levelname)s : %(message)s')
    fh.setFormatter(file_formater)

    logger.addHandler(fh)

    logger.info('用户{0}还款{1}元账户余额为{2}元'.format(username, repay_amount, user_money))


def logging_add_account(username, new_username):
    logger = logging.getLogger('transfer')
    logger.setLevel(logging.DEBUG)

    fh = handlers.RotatingFileHandler(
        filename=os.path.join(BASE_DIR, 'log/%s_add_account.log' % username), maxBytes=1024 * 1024, backupCount=100)
    fh.setLevel(logging.DEBUG)

    file_formater = logging.Formatter('%(asctime)s : %(name)s : %(levelname)s : %(message)s')
    fh.setFormatter(file_formater)

    logger.addHandler(fh)

    logger.info('用户{0}创建了新账户,账户名为:{1}'.format(username, new_username))


def logging_frozen_account(username):
    logger = logging.getLogger('transfer')

    fh = handlers.RotatingFileHandler(
        filename=os.path.join(BASE_DIR, 'log/%s_frozen_account.log' % username), maxBytes=1024 * 1024, backupCount=100)

    file_formater = logging.Formatter('%(asctime)s : %(name)s : %(levelname)s : %(message)s')
    fh.setFormatter(file_formater)

    logger.addHandler(fh)

    logger.warning('用户%s冻结了账户' % username)
