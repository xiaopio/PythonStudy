# _*_ encoding: utf-8 _*_
"""
PyCharm 34-字符串
2025年07月14日 16时53分06秒
by LiXiaoYang
"""

name = 'Jack and Rose'

value1 = name[0]
value2 = name[-1]
print(value1, value2)

# 字符串不能通过下标进行修改

index = name.index('and')
# 5
print(index)

name_replaced = name.replace("Rose", "Tom")
# Jack and Tom
print(name_replaced)

# split方法
my_str1 = "Hello World, this is my first class"
my_str_split_list = my_str1.split(" ")
# ['Hello', 'World,', 'this', 'is', 'my', 'first', 'class']
print(my_str_split_list)

# strip方法
my_str2 = " Hello World, this is my first class "
my_str_strip1 = my_str2.strip()
# Hello World, this is my first class 去除首位的空格
print(my_str_strip1)

my_str3 = "12Hello World, this is my first class21"
my_str_strip2 = my_str3.strip("12")
# Hello World, this is my first class
print(my_str_strip2)

my_str4 = "Hello World, this is my first class"
count = my_str4.count("s")
# 5
print(count)

i = len(my_str4)
# 35
print(i)

my_str = "123456"
index = 0
while index < len(my_str):
    print(my_str[index])
    index += 1

for item in my_str:
    print(item)

_str = "You are a teenager"
count = _str.count("a")
# 3
print(count)
str_replace = _str.replace(" ", "|")
# You|are|a|teenager
print(str_replace)
str_replace_split = str_replace.split("|")
# ['You', 'are', 'a', 'teenager']
print(str_replace_split)
