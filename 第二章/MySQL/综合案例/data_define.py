# _*_ encoding: utf-8 _*_
"""
PyCharm data_define
2025年07月17日 15时51分12秒
by LiXiaoYang
"""


class Record:
    def __init__(self, date, order_id, money, province):
        self.date = date            # 订单日期
        self.order_id = order_id    # 订单id
        self.money = money          # 销售额
        self.province = province    # 省份

    def __str__(self):
        return f"{self.date}, {self.order_id}, {self.money}, {self.province}"
