# _*_ encoding: utf-8 _*_
"""
PyCharm 08_正则表达式
2025年07月19日 10时37分39秒
by LiXiaoYang
"""

import re

s = "python java python python python"
# match 从头开始匹配
# result = re.match("python", s)
result = re.match("java", s)
# (0, 6)
# print(result.span())
# None
print(result)

result = re.search('java', s)
# <re.Match object; span=(7, 11), match='java'>返回第一个匹配的搜索结果
print(result)

result = re.findall('python', s)
# ['python', 'python', 'python', 'python']
# 没有返回空的list    []
print(result)
