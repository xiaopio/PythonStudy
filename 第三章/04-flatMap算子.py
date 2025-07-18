# _*_ encoding: utf-8 _*_
"""
PyCharm 04-flatMap算子
2025年07月18日 10时48分55秒
by LiXiaoYang
"""

from pyspark import SparkConf, SparkContext

import os

os.environ['PYSPARK_PYTHON'] = "D:/Programs/Anaconda3/python.exe"

conf = SparkConf().setMaster("local[*]").setAppName("test_spark")

sc = SparkContext(conf=conf)

rdd = sc.parallelize(["apple orange banana", "black red blue", "C# Java Python"])

rdd2 = rdd.map(lambda x: x.split(" "))
# [['apple', 'orange', 'banana'], ['black', 'red', 'blue'], ['C#', 'Java', 'Python']]
print(rdd2.collect())

rdd3 = rdd.flatMap(lambda x: x.split(" "))
# ['apple', 'orange', 'banana', 'black', 'red', 'blue', 'C#', 'Java', 'Python']
print(rdd3.collect())
