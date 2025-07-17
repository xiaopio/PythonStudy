# _*_ encoding: utf-8 _*_
"""
PyCharm 03-综合案例
2025年07月17日 15时36分25秒
by LiXiaoYang
"""

# 日期、订单id、销售额、销售省份

from file_define import FileReader, JSONFileReader, TextFileReader
from data_define import Record
from pyecharts.charts import Bar
from pyecharts.options import *
from pyecharts.globals import ThemeType

text_file_reader = TextFileReader('2011年1月销售数据.txt')
json_file_reader = JSONFileReader('2011年2月销售数据JSON.txt')

jan_data: list[Record] = text_file_reader.read_data()
feb_data: list[Record] = json_file_reader.read_data()

# 将两个月份的数据合并成一个list存储

all_data: list[Record] = jan_data + feb_data

data_dict = {}
for record in all_data:
    if record.date in data_dict.keys():
        data_dict[record.date] += record.money
    else:
        data_dict[record.date] = record.money

bar = Bar(init_opts=InitOpts(width="600px", height="600px", theme=ThemeType.LIGHT))

bar.add_xaxis(list(data_dict.keys()))

bar.add_yaxis("销售额", list(data_dict.values()), label_opts=LabelOpts(is_show=False))

bar.set_global_opts(
    title_opts=TitleOpts(title="每日销售额")
)

bar.render("每日销售额柱状图.html")
print("成功生成 每日销售额柱状图.html 请在浏览器中打开查看")
