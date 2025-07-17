# _*_ encoding: utf-8 _*_
"""
PyCharm 33-元组
2025年07月14日 16时07分49秒
by LiXiaoYang
"""

# 元组一旦完成定义，不可修改
(1, 2, 3, "Hello", True)
nums = (1, 2, 3, "Hello", True)

t1 = ()
t2 = tuple()
# t1的类型是<class 'tuple'>，内容是()
print(f"t1的类型是{type(t1)}，内容是{t1}")

# 定义一个元组只有一个数据，数据后要加 ,
t3 = (1)
# t3的类型是<class 'int'>，内容是1
print(f"t3的类型是{type(t3)}，内容是{t3}")
t3 = (1,)
# t3的类型是<class 'tuple'>，内容是(1,)
print(f"t3的类型是{type(t3)}，内容是{t3}")

# 元组的嵌套
t4 = ((1, 2, 3), (4, 5, 6))
# t4的类型是<class 'tuple'>，内容是((1, 2, 3), (4, 5, 6))
print(f"t4的类型是{type(t4)}，内容是{t4}")

i = t4[1][2]
# 6
print(i)

t6 = (1, 2, 3)
index = t6.index(1)
# 0
print(index)

count = t6.count(1)
# 1
print(count)
len1 = len(t6)
# 3
print(len1)

index = 0
while index < len(t6):
    print(t6[index])
    index += 1

for item in t6:
    print(item)

# 元组的“不可修改”特性指的是元组本身的结构不可变（即元组中的元素的数量和引用关系不能改变）
# 元素是不可变元素（整数、字符串、元组），不可以进行修改，但是元组中如果嵌套了可变元素（列表、字典、集合）里的内容可以修改，原因是元组中存放的是元素的引用（内存地址）
t7 = (1, 2, 3, [4, 5, 6])
# (1, 2, 3, [4, 5, 6])
print(t7)

t7[3][2] = 7
# (1, 2, 3, [4, 5, 7])
print(t7)

zhou = ('周杰伦', 11, ['football', 'music'])
index = zhou.index(11)
print(index)

print(zhou[0])

del zhou[2][0]
print(zhou)

zhou[2].append('coding')
print(zhou)
