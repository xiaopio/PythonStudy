# _*_ encoding: utf-8 _*_
"""
PyCharm 01-学生系统
2025年07月17日 09时05分19秒
by LiXiaoYang
"""


class Student:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def __str__(self):
        return f"【学生姓名：{self.name}，年龄：{self.age}，地址：{self.address}】"


total = 10
i = 1
while i <= total:
    name = None
    age = None
    address = None
    print(f"当前录入第{i}位学生信息，总共需录入{total}")
    name = input("请输入学生姓名：")
    age = input("请输入学生年龄：")
    address = input("请输入学生地址：")
    student = Student(name, age, address)
    print(f"学生{i}信息录入完成，信息为：{student}")
    i += 1
