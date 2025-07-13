# _*_ encoding: utf-8 _*_
"""
PyCharm 27-continue和break
2025年07月13日 19时14分05秒
by LiXiaoYang
"""
from typing import *

for i in range(10):
    print("你好")
    for j in range(10):
        print("不好")
        print(j)
        continue
        print("还好")

for i in range(10):
    print("好好好")
    break
    print("中中中")

print("行行行")


def main():
    return None
