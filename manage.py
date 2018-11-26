from shopping_mall import shopping
from atm import atm

def main():
    while True:
        info = '''
        ---------- 欢迎来到宇宙银行 ----------
        您要：
            1.进入购物商城
            2.使用ATM
            3.退出
        '''
        print(info)
        user_input = input('>>>').strip()
        if user_input.isdigit() and len(user_input):
            if user_input == '1':
                shopping.shopping_car()
            elif user_input == '2':
                atm.atm()
            elif user_input == '3':
                print('欢迎下次光临')
                break
            else:
                print('您的输入有误')
        else:
            print('您的输入有误')


if __name__ == '__main__':
    main()
