# _*_ encoding: utf-8 _*_
"""
PyCharm 01-闭包
2025年07月18日 16时33分04秒
by LiXiaoYang
"""

# 闭包
"""
优点：
    无需定义全局变量即可实现通过函数，持续的访问、修改某一个值
    闭包使用的变量的作用域在函数内，难以被错误的调用修改
缺点：
    由于内部函数持续引用外部函数的值，所以会导致这一部分内存空间不被释放，一直占用内存
"""


# def outer(logo):
#     def inner(msg):
#         print(f"<{logo}>{msg}<{logo}>")
#
#     return inner
#
#
# fun = outer("Donald J. Trump")
#
# fun("Make American great again!")

def outer():
    total = int(input("请输入银行卡余额:"))

    def inner():
        nonlocal total
        num = int(input("请输入存款金额："))
        total -= num
        print(f"本次取款{num}，银行卡余额：{total}")

    return inner


fun_check_out = outer()

fun_check_out()
fun_check_out()
fun_check_out()
fun_check_out()
