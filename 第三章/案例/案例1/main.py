# _*_ encoding: utf-8 _*_
"""
PyCharm main
2025年07月18日 14时56分06秒
by LiXiaoYang
"""

from pyspark import SparkConf, SparkContext

import os

os.environ['PYSPARK_PYTHON'] = "D:/Programs/Anaconda3/python.exe"

conf = SparkConf().setMaster("local[*]").setAppName("test_spark")

sc = SparkContext(conf=conf)

rdd = sc.textFile("hello.txt")

rdd2 = rdd.flatMap(lambda x: x.split(" "))
word_with_one = rdd2.map(lambda word: (word, 1))

count = word_with_one.reduceByKey(lambda a, b: a + b)
print(count.collect())
count_sort = count.sortBy(lambda x: x[1], ascending=True, numPartitions=1)
# [('Blue', 1), ('Orange', 1), ('apple', 5), ('Java', 6), ('python', 7)]
print(count_sort.collect())
