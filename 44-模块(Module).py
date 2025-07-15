# _*_ encoding: utf-8 _*_
"""
PyCharm 44-模块(Module)
2025年07月15日 11时08分19秒
by LiXiaoYang
"""

# [from 模块名] import [模块 | 类 | 变量 | 函数 | *] [as 别名]

# import time
#
# print("你好")
# time.sleep(5)
# print("en")
#
#
# from time import sleep
# print("你好")
# sleep(5)
# print("en")
#
# from time import *
# print("hello")
# sleep(5)
# print("hi")

# import time as t
# print("hello")
# t.sleep(5)
# print("hi")

# 导入自定义模块
# import my_module1
# from my_module1 import test
# my_module1.test(1, 2)
# test(1, 2)


from my_module1 import *
test(1, 2)
test2()
# NameError: name 'test3' is not defined. Did you mean: 'test'?
# test3()