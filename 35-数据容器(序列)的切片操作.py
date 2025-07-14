# _*_ encoding: utf-8 _*_
"""
PyCharm 35-数据容器(序列)的切片操作
2025年07月14日 20时08分34秒
by LiXiaoYang
"""

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

result1 = my_list[1:4]
# 结果1:[1, 2, 3]
print(f"结果1:{result1}")

my_tuple = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# 起始和结束不写表示从头到尾，步长为1可以省略
result2 = my_tuple[:]
# 结果2:(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print(f"结果2:{result2}")

my_str = "0123456789"
# 步长为2表示跳过 2 - 1 个元素取
result3 = my_str[::2]
# 结果3:02468
print(f"结果3:{result3}")

# 倒序切片

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

result4 = my_list[6:2:-3]
# 结果4:[6, 3]
print(f"结果4:{result4}")

my_tuple = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

result5 = my_tuple[::-2]
# 结果5:(9, 7, 5, 3, 1)
print(f"结果5:{result5}")

my_str = "0123456789"

result6 = my_str[::-1]  # 等同于将序列反转
# 结果6:9876543210
print(f"结果6:{result6}")

_str = "堂古尚 茶英公蒲 加添无 茶好然天"

tea_name = _str[4:8:1][::-1]
print(tea_name)

new_str = ""
str_split_list = _str.split(" ")
# print(str_split_list)
tea_name2 = str_split_list[1][::-1]
print(tea_name2)
