# _*_ encoding: utf-8 _*_
"""
PyCharm 06-封装
2025年07月17日 10时18分41秒
by LiXiaoYang
"""


# 定义一个类，内含私有成员变量、私有成员方法

class Phone:
    __current_voltage = 0.5

    def __keep_single_core(self):
        print("让CPU以单核模式运行")

    def call_by_5g(self):
        if self.__current_voltage >= 1:
            print("5g通话已开启")
        else:
            self.__keep_single_core()
            print("电量不足，无法使用5g通话，并已设置为单核模式运行")


phone = Phone()

# phone.__keep_single_core()
# print(phone.__current_voltage)

phone.call_by_5g()
