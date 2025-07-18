# _*_ encoding: utf-8 _*_
"""
PyCharm 02-数据输入
2025年07月18日 10时21分43秒
by LiXiaoYang
"""

from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local[*]").setAppName("test_spark")

sc = SparkContext(conf=conf)

# # 通过parallelize方法将Python对象加载到Spark内，成为RDD对象
# rdd1 = sc.parallelize([1, 2, 3, 4, 5])
# rdd2 = sc.parallelize((1, 2, 3, 4, 5))
# rdd3 = sc.parallelize("abcdefg")
# rdd4 = sc.parallelize({1, 2, 3, 4, 5})
# rdd5 = sc.parallelize({"key1": "value1", "key2": "value2"})
#
# # [1, 2, 3, 4, 5]
# print(rdd1.collect())
# # [1, 2, 3, 4, 5]
# print(rdd2.collect())
# # ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# print(rdd3.collect())
# # [1, 2, 3, 4, 5]
# print(rdd4.collect())
# # ['key1', 'key2']
# print(rdd5.collect())

# 通过textFile方法，读取文件数据加载到Spark内，成为RDD对象
rdd = sc.textFile("测试.txt")
print(rdd.collect())

sc.stop()
