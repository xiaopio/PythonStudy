# _*_ encoding: utf-8 _*_
"""
PyCharm 02-基础准备
2025年07月18日 08时46分05秒
by LiXiaoYang
"""
# 导包
from pyspark import SparkConf, SparkContext

# 构建SparkConf类对象
conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")

# 基于SparkConf类对象创建SparkContext对象
sc = SparkContext(conf=conf)

# 打印PySpark的运行版本
print(sc.version)

# 停止SparkContext对象的运行（停止PySpark程序）
sc.stop()
