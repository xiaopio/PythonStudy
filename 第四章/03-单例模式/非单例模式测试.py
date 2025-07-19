# _*_ encoding: utf-8 _*_
"""
PyCharm 非单例模式测试
2025年07月18日 17时17分46秒
by LiXiaoYang
"""


class StrTools:
    pass


str1 = StrTools()
str2 = StrTools()
# <__main__.StrTools object at 0x0000022704ED4710>
print(str1)
# <__main__.StrTools object at 0x0000022704ED4390>
print(str2)
