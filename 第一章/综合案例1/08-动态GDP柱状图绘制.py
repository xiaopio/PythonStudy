# _*_ encoding: utf-8 _*_
"""
PyCharm 08-动态GDP柱状图绘制
2025年07月16日 14时54分48秒
by LiXiaoYang
"""

# 列表的sort方法
my_list = [["a", 33], ["b", 44], ["c", 55]]


def choose_sort_key(element):
    return element[1]


# my_list.sort(key=choose_sort_key, reverse=True)

my_list.sort(key=lambda element: element[1], reverse=True)

print(my_list)
