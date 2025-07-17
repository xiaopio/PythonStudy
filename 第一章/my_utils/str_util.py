# _*_ encoding: utf-8 _*_
"""
PyCharm str_util
2025年07月15日 14时58分56秒
by LiXiaoYang
"""


def str_reverse(s):
    """
    反转字符串
    :param s: 字符串
    :return: 反转后的字符串
    """
    return s[::-1]


def substr(s, x: int, y: int):
    """
    按照下标x和y将字符串切片
    :param s: 字符串
    :param x:起始下标
    :param y: 结束下标
    :return: 切片后的字符串
    """
    return s[x:y]


if __name__ == '__main__':

    print(str_reverse('hello'))

    print(substr("helloworld", 1, 4))
