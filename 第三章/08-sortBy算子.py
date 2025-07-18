from pyspark import SparkConf, SparkContext
import os

# 设置Python
os.environ['PYSPARK_PYTHON'] = "D:/Programs/Anaconda3/python.exe"
os.environ['PYSPARK_DRIVER_PYTHON'] = "D:/Programs/Anaconda3/python.exe"

# 创建Spark配置
conf = SparkConf() \
    .setMaster("local[*]") \
    .setAppName("test_spark") \
    .set("spark.python.worker.faulthandler.enabled", "true")  # 获取更详细的Python错误

# 创建Spark上下文
sc = SparkContext(conf=conf)

try:
    # 测试简单RDD操作
    print("测试基础功能:")
    test_rdd = sc.parallelize([1, 2, 3])
    print(test_rdd.collect())

    # 执行你的原始代码
    print("\n执行排序操作:")
    rdd = sc.parallelize([("a", 11, "你好"), ("b", 9, "哈哈")])
    final_rdd = rdd.sortBy(lambda x: x[1], ascending=True)
    # [('b', 9, '哈哈'), ('a', 11, '你好')]
    print("排序结果:", final_rdd.collect())

except Exception as e:
    print(f"执行过程中发生错误: {e}")
finally:
    # 确保Spark上下文被关闭
    if sc:
        sc.stop()
        print("Spark上下文已关闭")
