# _*_ encoding: utf-8 _*_
"""
PyCharm 04-构造方法
2025年07月17日 08时57分16秒
by LiXiaoYang
"""


# 构造方法名称 __init__
class Student:
    # name = None
    # age = None
    # gender = None
    # tel = None

    def __init__(self, name, age, gender, tel):
        self.name = name
        self.age = age
        self.gender = gender
        self.tel = tel
        print("Student类创建了一个对象")


student1 = Student('张三', 18, '男', '18457521457')
print(student1.name)
print(student1.age)
print(student1.gender)
print(student1.tel)


