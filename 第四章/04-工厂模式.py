# _*_ encoding: utf-8 _*_
"""
PyCharm 04-工厂模式
2025年07月19日 09时16分02秒
by LiXiaoYang
"""

"""
工厂模式
    将对象的创建由使用原生类本身创建
    转换到由特定的工厂方法来创建
    优点：
        大批量创建对象时有统一的入口，易于代码维护
        当发生修改时，仅修改工厂类的创建方法即可
        符合现实世界的模式，即由工厂来制作产品（对象）
"""


class Person:
    pass


class Worker(Person):
    pass


class Student(Person):
    pass


class Teacher(Person):
    pass


class PersonFactory:
    def get_person(self, p_type):
        if p_type == 'w':
            return Worker()
        if p_type == 's':
            return Student()

        if p_type == 't':
            return Teacher()


pf = PersonFactory()

worker = pf.get_person('w')

student = pf.get_person('s')

teacher = pf.get_person('t')
