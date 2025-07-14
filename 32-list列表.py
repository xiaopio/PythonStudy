# _*_ encoding: utf-8 _*_
"""
PyCharm 32-list列表
2025年07月14日 11时48分44秒
by LiXiaoYang
"""
from typing import *

# 字面量
# 列表中可以存储不同的数据类型,支持嵌套
["张三", "李四", 666, True, [1, 2, 3]]
# 变量
student = ["张三", "李四", "王五", "赵六"]
# 定义空列表
name = []
city = list()

# 列表的下标索引
# 0 表示第一个元素,从左往右
print(student[0])
# -1 表示最后一个元素,从右往左
print(student[-1])

# 嵌套列表取元素

city = [["郑州", "洛阳", "新乡"], ["廊坊", "邯郸", "石家庄"]]
print(city[0][0])
for i in city:
    for j in i:
        print(j)

mylist = [1, 2, 3]

# 获取列表元素的下标
index = mylist.index(2)
# 1
print(index)

# 更改列表元素的值
mylist[1] = 3
# [1, 3, 3]
print(mylist)

# 列表下标位置插入一个元素
mylist.insert(2, 4)
# [1, 3, 4, 3]
print(mylist)

# 追加单个元素
mylist.append(5)
# [1, 3, 4, 3, 5]
print(mylist)

# 追加多个元素
mylist.extend([1, 2, 3, 4, 5])
# [1, 3, 4, 3, 5, 1, 2, 3, 4, 5]
print(mylist)

# 列表删除元素
del mylist[2]
# [1, 3, 3, 5, 1, 2, 3, 4, 5]
print(mylist)

# 将指定下标的元素移除并返回
pop_num = mylist.pop(0)
# 1
print(pop_num)
# [3, 3, 5, 1, 2, 3, 4, 5]
print(mylist)

# 删除某元素在列表中的第一个匹配项
mylist.remove(3)
# [3, 5, 1, 2, 3, 4, 5]
print(mylist)

# 清空列表内容
mylist.clear()
# []
print(mylist)

mylist.extend([1, 2, 3, 4, 5, 2, 2, 2])
# 统计某元素在列表中的数量
count = mylist.count(2)
# 4
print(count)

# 统计列表中一共有多少元素
mylist_len = len(mylist)
# 8
print(mylist_len)

stu_age = [21, 25, 21, 23, 22, 20]

stu_age.append(31)
print(stu_age)
stu_age.extend([29, 33, 30])
print(stu_age)
element1 = stu_age.pop(0)
element2 = stu_age.pop(-1)
print(element1, element2)
# [25, 21, 23, 22, 20, 31, 29, 33]
print(stu_age)
age_index = stu_age.index(31)
# 5
print(age_index)

provinces = ["北京", "上海", "广州", "深圳"]


# 列表的遍历
def list_while_func(_list: list):
    """
    使用 while循环 遍历列表演示函数
    :param _list: 要遍历的列表
    :return: None
    """
    index = 0
    while index < len(_list):
        print(list[index])
        index += 1


list_while_func(provinces)


def list_for_func(_list: list):
    """
    使用 for循环 遍历列表演示函数
    :param _list: 要遍历的列表
    :return: None
    """
    for item in _list:
        print(item)


list_for_func(provinces)

# 遍历一个列表，将列表中的偶数全部取出放入一个新的列表

num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list = []
index = 0
while index < len(num_list):
    if num_list[index] % 2 == 0:
        new_list.append(num_list[index])
    index += 1
# [2, 4, 6, 8, 10]
print(new_list)

new_list = []
for item in num_list:
    if item % 2 == 0:
        new_list.append(item)
# [2, 4, 6, 8, 10]
print(new_list)
