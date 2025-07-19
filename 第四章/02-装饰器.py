# _*_ encoding: utf-8 _*_
"""
PyCharm 02-装饰器
2025年07月18日 17时00分47秒
by LiXiaoYang
"""
"""
装饰器
    创建一个闭包函数，在闭包函数内调用目标函数
    可以达到不改动目标函数的同时，增加额外的功能
"""


# 装饰器的一般写法（闭包）
# def outer(func):
#     def inner():
#         print("我碎觉了......")
#         func()
#         print("我起床了......")
#
#     return inner
#
#
# def sleep():
#     import random
#     import time
#     print("睡眠中......")
#     time.sleep(random.randint(1, 5))
#
#
# fn = outer(sleep)
# fn()

# 装饰器的快捷写法（语法糖）

def outer(func):
    def inner():
        print("我碎觉了......")
        func()
        print("我起床了......")

    return inner


@outer
def sleep():
    import random
    import time
    print("睡眠中......")
    time.sleep(random.randint(1, 5))


sleep()
