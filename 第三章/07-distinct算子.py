# _*_ encoding: utf-8 _*_
"""
PyCharm 07-distinct算子
2025年07月18日 15时10分02秒
by LiXiaoYang
"""
# distinct() 去重操作
from pyspark import SparkConf, SparkContext
import os

os.environ['PYSPARK_PYTHON'] = "D:/Programs/Anaconda3/python.exe"

conf = SparkConf().setMaster("local[*]").setAppName("test_spark")

sc = SparkContext(conf=conf)

rdd = sc.parallelize([1, 1, 3, 3, 5, 5, 7, 8, 8, 9, 10])

rdd2 = rdd.distinct()
# [1, 3, 5, 7, 8, 9, 10]
print(rdd2.collect())
