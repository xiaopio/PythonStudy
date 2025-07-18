# _*_ encoding: utf-8 _*_
"""
PyCharm 06-filter方法
2025年07月18日 15时03分20秒
by LiXiaoYang
"""

from pyspark import SparkConf, SparkContext
import os

os.environ['PYSPARK_PYTHON'] = "D:/Programs/Anaconda3/python.exe"

conf = SparkConf().setMaster("local[*]").setAppName("test_spark")

sc = SparkContext(conf=conf)

rdd = sc.parallelize([1, 2, 3, 4, 5])

# 过滤，只保留奇数
rdd2 = rdd.filter(lambda x: x % 2 == 1)
# [1, 3, 5]
print(rdd2.collect())
