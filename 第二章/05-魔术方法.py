# _*_ encoding: utf-8 _*_
"""
PyCharm 05-魔术方法
2025年07月17日 09时20分06秒
by LiXiaoYang
"""


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # __str__魔术方法
    def __str__(self):
        return f"姓名：{self.name}，年龄：{self.age}"

    # __lt__魔术方法
    def __lt__(self, other):
        # return self.age < other.age
        return self.age < other.age

    # __le__魔术方法
    def __le__(self, other):
        return self.age <= other.age

    # __eq__魔术方法
    def __eq__(self, other):
        return self.age == other.age


student1 = Student("张三", 18)
# <__main__.Student object at 0x00000260D65983E0>
print(student1)

# __str__魔术方法
# 姓名：张三，年龄：18
print(student1)

# __lt__魔术方法
student2 = Student("李四", 20)
# True
print(student1 < student2)
# False
print(student1 > student2)

# __le__魔术方法
# True
print(student1 <= student2)
# False
print(student1 >= student2)

# __eq__魔术方法
# False
print(student1 == student2)
# True
print(student1 != student2)
