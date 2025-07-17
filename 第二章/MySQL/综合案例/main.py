# _*_ encoding: utf-8 _*_
"""
PyCharm 03-综合案例
2025年07月17日 15时36分25秒
by LiXiaoYang
"""
from collections import namedtuple

# 日期、订单id、销售额、销售省份

from file_define import FileReader, JSONFileReader, TextFileReader
from data_define import Record
from pymysql import Connection

text_file_reader = TextFileReader('2011年1月销售数据.txt')
json_file_reader = JSONFileReader('2011年2月销售数据JSON.txt')

jan_data: list[Record] = text_file_reader.read_data()
feb_data: list[Record] = json_file_reader.read_data()

# 将两个月份的数据合并成一个list存储

all_data: list[Record] = jan_data + feb_data

# data_dict = {}

conn = Connection(host='localhost', port=3306, user='root', password='123456', autocommit=True)
cursor = conn.cursor()
conn.select_db('py_sql')

# for record in all_data:
#     sql = (f"insert into orders(order_date, order_id, money, province) "
#            f"values('{record.date}', '{record.order_id}', {record.money}, '{record.province}')")
#     # print(sql)
#     cursor.execute(sql)
sql = 'select * from orders;'
cursor.execute(sql)
result = cursor.fetchall()
f = open("销售数据.txt", "a", encoding="utf-8")
for r in result:
    data_tuple = r
    Order = namedtuple('Order', ["date", "order_id", "money", "province"])
    order_obj = Order(*data_tuple)
    result_dict = {
        "date": order_obj.date.strftime("%Y-%m-%d"),
        "order_id": order_obj.order_id,
        "money": order_obj.money,
        "province": order_obj.province
    }
    f.write(f'{result_dict}\n')

f.close()
conn.close()
