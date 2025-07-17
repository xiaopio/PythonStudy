# _*_ encoding: utf-8 _*_
"""
PyCharm 44-自定义模块
2025年07月15日 11时18分52秒
by LiXiaoYang
"""

__all__ = ['test', 'test2']


def test(a, b):
    print(a + b)

# 这样写在外部导入时会执行
# test(1, 2)


def test2():
    print('test2')


def test3():
    print('test3')


# 如果我想对模块进行测试,将测试文件写入main中
if __name__ == '__main__':
    # 这样在模块被调用时,这里不会被执行
    test(1, 2)
