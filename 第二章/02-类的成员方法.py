# _*_ encoding: utf-8 _*_
"""
PyCharm 02-类的成员方法
2025年07月17日 08时46分24秒
by LiXiaoYang
"""


# 成员方法的定义和使用
class Student:
    name = None

    def say_hi(self):
        print(f"hi，大家好，我是{self.name}")

    def say_hi2(self, msg):
        print(f"大家好，我是{self.name}，{msg}")


student = Student()
student.name = '周杰伦'
student.say_hi()
student.say_hi2('我是渣渣灰')
