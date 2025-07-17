# _*_ encoding: utf-8 _*_
"""
PyCharm 30-函数综合案例
2025年07月14日 10时45分57秒
by LiXiaoYang
"""
# from typing import *
name = None
balance = 5000000

name = input("请输入您的姓名：")


def check_balance():
    """
    查询余额
    :return: 余额
    """
    print(f"{name}，您好，当前您的账户余额：{balance}元")


def deposit_money(deposit_amount: int):
    """
    存款
    :param deposit_amount: 存款金额
    :return: 存款成功提示
    """
    global balance
    balance += deposit_amount
    print(f"{name}，您好，本次存款{deposit_amount}元成功")


def takeout_money(takeout_amount: int):
    """
    取款
    :param takeout_amount: 取款金额
    :return: 取款成功提示
    """
    global balance
    balance -= takeout_amount
    print(f"{name}，您好，本次取款{takeout_amount}元成功")


def main():
    """
    Haust银行系统主程序
    :return: None
    """
    global name
    # flag = True
    # while flag:
    # 这里加上 continue break关键字更加严谨
    while True:
        print("---------------------主菜单---------------------")
        print(f"{name}，您好，欢迎使用Haust银行24小时自助ATM，请选择操作：")
        print("查询余额\t[输入1]\n存款\t\t[输入2]\n取款\t\t[输入3]\n退出\t\t[输入4]")
        print("-----------------------------------------------")
        chose = int(input("请输入您的选择："))
        if chose == 1:
            print("--------------------查询余额--------------------")
            check_balance()
            continue
        elif chose == 2:
            print("----------------------存款----------------------")
            deposit_money(int(input(f"{name}，您好，请输入您的存款金额：")))
            check_balance()
            continue
        elif chose == 3:
            print("----------------------取款----------------------")
            takeout_money(int(input(f"{name}，您好，请输入您的取款金额：")))
            check_balance()
            continue
        elif chose == 4:
            print("---------------------退出成功--------------------")
            # flag = False
            break


main()
