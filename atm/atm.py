from settings.settings import BASE_DIR
from . import withdraw
from . import transfer
from . import repayment
from . import show_consume
from . import account
from utils import user_verify


@user_verify.user_verify
def atm_entrance(username, user_money, *args, **kwargs):
    info = '''
    '---------- 欢迎使用宇宙银行ATM机 ----------'
    请选择要办理的业务：
    1.提现
    2.转账
    3.还款
    4.显示消费流水
    5.管理账户
    6.返回上一层
    '''
    while True:
        print(info)
        choice = input('>>>').strip()
        if choice == '1':
            withdraw.withdraw_money(username, user_money)
        elif choice == '2':
            transfer.transfer_money(username, user_money)
        elif choice == '3':
            repayment.repayment_money(username, user_money)
        elif choice == '4':
            show_consume.water_consumption(username)
        elif choice == '5':
            account.manage_account(username, user_money)
        elif choice == '6':
            break
        else:
            print('输入不合法，请按提示输入数字')
