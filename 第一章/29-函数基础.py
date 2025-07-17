# _*_ encoding: utf-8 _*_
"""
PyCharm 29-函数基础
2025年07月13日 22时32分35秒
by LiXiaoYang
"""

import random


# from typing import *


def my_len(data):
    """
    统计数据长度
    :param data: 数据
    :return: 长度
    """
    return sum(1 for _ in data)


count = my_len([1, 2, 3, 4, 5])
print(count)


def say_hi():
    """
    说：hi
    :return: 打印 hi
    """
    return "hi"


print(say_hi())


def health_code(institution_name: str, time: int, body_temperature: float):
    """
    防疫检测
    :param institution_name: 机构名称
    :param time: 核酸证明限制时间
    :param body_temperature: 体温
    :return: 核酸提示信息
    """
    if body_temperature <= 37.5:
        return f"欢迎来到{institution_name}!\n请出示您的健康码以及{time}小时核酸证明！\n体温测量中，您的体温是{body_temperature}°，体温正常，请进！"
    else:
        return f"欢迎来到{institution_name}!\n请出示您的健康码以及{time}小时核酸证明！\n体温测量中，您的体温是{body_temperature}°，体温异常，需要隔离！"


print(health_code("haust大学", 72, round(random.uniform(36, 42), 1)))


def add(a: int, b: int):
    """
    两个整数相加
    :param a: 整数
    :param b: 整数
    :return: 两个整数相加的和
    """
    return a + b


print(add(1, 2))


def add(a: int, b: int):
    print(a + b)
    # 手动返回None效果一样
    return None


result = add(1, 2)
# None
print(f"无返回值的函数，返回的内容是{result}")
# <class 'NoneType'>
print(f"无返回值函数，返回的内容类型是{type(result)}")


def check_age(age: int):
    """
    检查年龄是否满18岁
    :param age: 年龄
    :return: 满 18 return "SUCCESS"，否则 return None
    """
    return None if age < 18 else "SUCCESS"


result = check_age(16)
if not result:
    # None 在 if 判断中等同于 False
    print("未成年，不可以进入！")

# None 用于声明无初始内容的变量
name = None


# 函数的嵌套调用

def func_a():
    print("-----1-----")


def func_b():
    print("-----2-----")


def func_c():
    func_a()
    func_b()
    print("-----3-----")


func_c()

# 局部变量
# def test_a():
#     num = 100
#     print(num)
#
#
# test_a()


# Unresolved reference 'num'
# 想要在外部使用num，需要在函数外定义
# print(num)

num = 200


def test_b():
    # Unresolved reference 'num'
    # print(num)
    # 没使用 global 关键字，函数内部的 num 和外部的 num 不是同一个变量
    # Shadows name 'num' from outer scope
    # 提示你在 ** 局部作用域（如函数内部）中使用了与外部作用域（如全局变量）** 相同的变量名 num，这可能导致意外行为或降低代码可读性。
    # global 关键字声明num是全局变量
    global num
    num = 500
    # 500
    print(num)


test_b()
# 200
# 函数内修改 num，并不影响函数外的 num，需使用 global 关键字在函数内部声明变量为 全局变量
# 函数内部加上global关键字声明后，函数内部num值改变可以影响函数外的num值
# 500
print(num)



def main():
    return None
