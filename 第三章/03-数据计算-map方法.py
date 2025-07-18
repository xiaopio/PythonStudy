# _*_ encoding: utf-8 _*_
"""
PyCharm 03-数据计算-map方法
2025年07月18日 10时36分51秒
by LiXiaoYang
"""

from pyspark import SparkConf, SparkContext

import os

os.environ['PYSPARK_PYTHON'] = "D:/Programs/Anaconda3/python.exe"

conf = SparkConf().setMaster("local[*]").setAppName("test_spark")

sc = SparkContext(conf=conf)

rdd = sc.parallelize([1, 2, 3, 4, 5])

# def func(data):
#     return data * 10

# map算子
# 链式调用
rdd2 = rdd.map(lambda x: x * 10).map(lambda x: x + 5)

print(rdd2.collect())

sc.stop()
