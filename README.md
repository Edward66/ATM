# ATM
## Using basic python grammar realizes the function of ATM.

### 函数作业：模拟实现一个ATM + 购物商城程序

####1.额度 15000或自定义
####2.实现购物商城，买东西加入 购物车，调用信用卡接口结账
####3.可以提现，手续费5%
####4.支持多账户登录
####5.支持账户间转账
####6.记录每月日常消费流水
####7.提供还款接口
####8.ATM记录操作日志
####9.提供管理接口，包括添加账户、用户额度，冻结账户等。。。
####10.用户认证用装饰器

    .
    ├── README.md  
    ├── __init__.py
    ├── atm  atm功能
    │   ├── __pycache__
    │   ├── account.py  管理账户接口
    │   ├── atm.py    atm入口
    │   ├── credit_card.py   信用卡接口，在购物商城结账的时候用
    │   ├── repayment.py    还款接口
    │   ├── show_consume.py  显示消费流水接口
    │   ├── transfer.py   转账接口
    │   └── withdraw.py   取现接口
    ├── db   数据库，初始数据库由utils里的generated_db_info.py生成
    │   
    ├── log 消费记录和atm记录
    │   
    ├── manage.py 主程序入口
    ├── settings  环境配置
    │   ├── __pycache__
    │   └── settings.py
    ├── shopping_mall  购物商城
    │   ├── __pycache__
    │   └── shopping.py
    └── utils  工具
        ├── __init__.py
        ├── __pycache__
        ├── generated_db_info.py  生成初始用户信息和商品信息
        ├── logging_atm.py   生成atm操作的log文件
        ├── logging_consume.py  生成消费记录的log文件
        └── user_verify.py   用户认证登陆