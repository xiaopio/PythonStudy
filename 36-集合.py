# _*_ encoding: utf-8 _*_
"""
PyCharm 36-集合
2025年07月14日 20时42分24秒
by LiXiaoYang
"""
# 集合元素不重复且无序
my_set = {"1", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
my_set_empty = set()  # 定义空集合

# my_set的内容是：{'5', '1', '7', '6', '2', '8', '4', '3', '9'}，类型是<class 'set'>
print(f"my_set的内容是：{my_set}，类型是{type(my_set)}")
# my_set_empty的内容是：set()，类型是<class 'set'>
print(f"my_set_empty的内容是：{my_set_empty}，类型是{type(my_set_empty)}")

my_set.add("10")
# {'1', '10', '7', '8', '6', '9', '5', '3', '4', '2'}
print(my_set)

my_set.remove("10")
# {'1', '8', '7', '4', '5', '9', '2', '3', '6'}
print(my_set)

my_set_pop = my_set.pop()
# 随机取出
print(my_set_pop)

# 清空集合
my_set.clear()
# set() 空集合的意思
print(my_set)

set1 = {1, 2, 3}
set2 = {1, 4, 5}
set3 = set1.difference(set2)
# {2, 3} 取差集，集合1中有，集合2中没有的元素
print(set3)

# difference_update 取差集，集合1被修改，集合2不修改
set1.difference_update(set2)
# {2, 3}
print(set1)

set4 = set1.union(set2)
# {1, 2, 3, 4, 5}
print(set4)

count = len(set4)
# 5个
print(count)

for ele in set4:
    print(f"集合中的元素有:{ele}")

name_list = ["张三", "李四", "王五", "赵六", "孙二娘", "武松", "林冲", "鲁智深", "宋江", "孙二娘", "武松", "孙二娘", "武松"]
name_set = set()

for ele in name_list:
    name_set.add(ele)

print(name_set)
