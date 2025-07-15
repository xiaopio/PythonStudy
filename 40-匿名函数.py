# _*_ encoding: utf-8 _*_
"""
PyCharm 40-匿名函数
2025年07月15日 09时03分37秒
by LiXiaoYang
"""


# 函数作为参数传递
def compute(x, y):
    return x + y


def test_func(_compute):
    result = _compute(1, 2)
    # _compute的参数类型是：<class 'function'>
    print(f"_compute的参数类型是：{type(_compute)}")
    return result


print(test_func(compute))

# lambda 匿名函数
# 匿名函数只能临时使用一次
# 函数体只能写一行
# lambda 传入参数: 函数体(一行代码)
print(test_func(lambda x, y: x + y))
