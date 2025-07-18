# _*_ encoding: utf-8 _*_
"""
PyCharm main
2025年07月18日 16时23分58秒
by LiXiaoYang
"""

from pyspark import SparkConf, SparkContext

import os

os.environ['PYSPARK_PYTHON'] = "D:/Programs/Anaconda3/python.exe"

conf = SparkConf().setMaster("local[*]").setAppName("test_spark")

sc = SparkContext(conf=conf)

sc.textFile()
