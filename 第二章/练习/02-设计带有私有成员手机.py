# _*_ encoding: utf-8 _*_
"""
PyCharm 02-设计带有私有成员手机
2025年07月17日 10时31分07秒
by LiXiaoYang
"""


class Phone:
    __is_5g_enable = False  # 5g状态

    def __check_5g(self):
        if self.__is_5g_enable:
            print("5g开启")
        else:
            print("5g关闭，使用4g网络")

    def call_by_5g(self):
        self.__check_5g()
        print("正在通话中")


phone = Phone()
phone.call_by_5g()
