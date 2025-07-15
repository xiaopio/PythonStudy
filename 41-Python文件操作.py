# _*_ encoding: utf-8 _*_
"""
PyCharm 41-Python文件操作
2025年07月15日 09时20分15秒
by LiXiaoYang
"""
# import time

# 文件读取操作
# 打开文件
# f = open("D:/测试.txt", "r", encoding="utf-8")
# <class '_io.TextIOWrapper'>
# print(type(f))
# 读取文件 - read(num), num 读取多少字节，文本模式下为多少字符，为空读取全部

# 会记录你第一次读取的位置，第二次读取接着第二次继续读取
# print(f"第一次读取：{f.read(10)}")
# print(f"第二次读取：{f.read()}")

# 读取文件的全部行，封装到列表中
# lines = f.readlines()
# lines对象的类型是<class 'list'>
# print(f"lines对象的类型是{type(lines)}")

"""
lines对象的内容是['四年冬季烦恼的佛\n', '烦恼都发脾气就二篇\n', '按佛i阿娇批发价阿婆发\n', '发哦收费口【afk1\n',
                '哪里上课放假啊皮肤\n', '发泼附件二平方米\n', '十分惧怕设计费珀尔\n', '佛配件我']
"""
# print(f"lines对象的内容是{lines}")

# line1 = f.readline()
# line2 = f.readline()
# line3 = f.readline()

# print(line1, line2, line3)

# for 循环读取文件行
# for line in f:
#     print(line)

# time.sleep(500000)
# 关闭文件
# f.close()
# time.sleep(500000)

# with open 语法操作文件
# 执行完自动关闭文件
# with open("D:/测试.txt", "r", encoding="utf-8") as f:
#     for line in f:
#         print(line)
#
# time.sleep(500000)

# 练习 -- 单词计数
# with open("D:/测试.txt", "r", encoding="utf-8") as f:
#     txt = f.read()
#     """
#     whether the weather be fine or whether the weather be not.
#     whether the weather be cold or whether the weather be hot.
#     we'll weather the weather whether we like it or not.
#     """
#     print(txt)
#     count = txt.count("weather")
#     # 6
#     print(count)


# f = open("D:/测试.txt", "r", encoding="utf-8")

# count = f.read().count("weather")
# print(count)

# lines = f.readlines()
# count = 0
# for line in lines:
#     count += line.count("weather")
#
# print(count)

# count = 0
# for line in f:
#     # line.replace('\n', '')
#     line = line.strip()
#     print(line)
#     count += line.count("weather")
#
# print(count)
# f.close()

# 文件写入操作

# f = open("D:/测试.txt", "w", encoding="utf-8")
# # 文件存在会清空文件中原内容 文件不存在会创建文件
# f.write("hello world")
#
# # 内容刷新 内存 --> 外存
# f.flush()
# # 关闭文件
# f.close()

# 文件追加
# f = open("D:/测试.txt", "a", encoding="utf-8")
# # 文件不存在会创建文件 存在追加内容
# f.write("hello world\n")
#
# # 内容刷新 内存 --> 外存
# f.flush()
# # 关闭文件
# f.close()


