# _*_ encoding: utf-8 _*_
"""
PyCharm 05-reduceByKey算子
2025年07月18日 10时59分13秒
by LiXiaoYang
"""

from pyspark import SparkConf, SparkContext
import os

os.environ['PYSPARK_PYTHON'] = "D:/Programs/Anaconda3/python.exe"

conf = SparkConf().setMaster("local[*]").setAppName("test_spark")

sc = SparkContext(conf=conf)

rdd = sc.parallelize([('男', 99), ('女', 88), ('男', 77), ('女', 66)])

rdd2 = rdd.reduceByKey(lambda a, b: a + b)
# [('女', 154), ('男', 176)]
print(rdd2.collect())
