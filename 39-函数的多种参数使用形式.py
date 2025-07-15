# _*_ encoding: utf-8 _*_
"""
PyCharm 39-函数的多种参数使用形式
2025年07月15日 08时44分38秒
by LiXiaoYang
"""


def user_info(name, age, gender):
    print(f"您的姓名是{name}，年龄是{age}，性别是：{gender}")


# 位置参数 默认使用形式
user_info("张三", 18, "男")

# 关键字参数 key = value
user_info(name="小明", age=20, gender="男")
# 可以乱序
user_info(age=18, gender="女", name="小美")


# 当调用函数时没有传递参数，就会使用默认使用缺省参数对应的值
# 设置默认值必须放在最后
def emp_info(name, age, gender='男'):
    print(f"您的姓名是{name}，年龄是{age}，性别是：{gender}")


# 默认 gender = '男'
emp_info("Tom", 15)
emp_info('Rose', 15, gender='女')


# 不定长参数（可变参数）

# 位置传递
# 形参作为元组存在，将传入的参数合并为一个元组(tuple)
def stu_info(*args):
    print(args)


# ('Tom',)
stu_info('Tom')
# ('Tom', 15)
stu_info('Tom', 15)


# 关键字传递
# 字典
def tch_info(**kwargs):
    print(kwargs)


# {'name': 'Tom', 'age': 18, 'id': 10001}
tch_info(name='Tom', age=18, id=10001)
