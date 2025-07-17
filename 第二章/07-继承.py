# _*_ encoding: utf-8 _*_
"""
PyCharm 07-继承
2025年07月17日 10时40分52秒
by LiXiaoYang
"""


class Phone:
    IMEI = None  # 序列号
    producer = "HUAWEI⭕"  # 厂商

    def call_by_4g(self):
        print("4g通话中")


# 单继承
class PhonePure(Phone):
    face_id = '101351'  # 面部id

    def call_by_5g(self):
        print("使用5g通话")


phone_pure = PhonePure()

print(phone_pure.IMEI, phone_pure.producer, phone_pure.face_id)
phone_pure.call_by_4g()
phone_pure.call_by_5g()
print("----------------------------")


# 多继承

class NFCReader:
    nfc_type = '第五代'
    producer = 'HUAWEI●'

    def read_card(self):
        print("ncf 读卡")

    def write_card(self):
        print("nfc 写卡")


class RemoteControl:
    rc_type = '红外遥控'

    def control(self):
        print("红外遥控开启了")


class MyPhone(Phone, NFCReader, RemoteControl):
    pass


my_phone = MyPhone()

print(my_phone.producer)
my_phone.call_by_4g()
my_phone.read_card()
my_phone.write_card()
my_phone.control()
print("----------------------------")


# 复写
class PhoneMin(Phone):
    IMEI = 'sn5161616156'
    producer = 'HONER'

    def call_by_4g(self):
        # print(f"父类的厂商是{Phone.producer}")
        print(f"父类的厂商是{super().producer}")
        print("现在我是4g+")
        print("信号增强中")
        # Phone.call_by_4g()
        super().call_by_4g()


phone_min = PhoneMin()

print(phone_min.IMEI)
print(phone_min.producer)
phone_min.call_by_4g()
