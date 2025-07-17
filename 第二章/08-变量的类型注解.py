# _*_ encoding: utf-8 _*_
"""
PyCharm 08-变量的类型注解
2025年07月17日 14时31分47秒
by LiXiaoYang
"""
import json
import random
from typing import Union

# 基础数据类型注解
var_1: int = 10
var_2: str = "hello"
var_3: bool = True


# 类对象类型注解
class Student:
    pass


stu: Student = Student()

# 基础容器类型注解
my_list: list = [1, 2, 3]
my_tuple: tuple = (1, 2, 3)
my_dict: dict = {"hello": 666}

# 容器类型详细注解
my_list: list[int] = [1, 2, 3]
my_tuple: tuple[int, str, bool] = (1, "hello", True)
my_dict: dict[str, int] = {"hello": 666}

# 在注释中进行类型注解
var_1 = random.randint(1, 10)  # type:int
var_2 = json.loads('{"name": "张三"}')  # type:dict[str, str]


def func():
    return 10


var_3 = func()  # type: int


# 函数方法进行类型注解

def add(x: int, y: int):
    return x + y


add(1, 2)


# 对返回值进行类型注解
def func_1(data: list) -> list:
    return data


# Union联合类型注解
my_list: list[Union[str, int]] = [1, 2, "hello", "nushi"]
my_dict: dict[str, Union[str, int]] = {"name": "周杰伦", "age": 31}


def func_2(data: Union[int, str]) -> Union[int, str]:
    pass
