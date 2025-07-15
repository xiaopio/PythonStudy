# _*_ encoding: utf-8 _*_
"""
PyCharm 03-案例实现
2025年07月15日 18时30分07秒
by LiXiaoYang
"""
from get_data_module import get_diagnosed_data as get_data
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LabelOpts

us, us_update_date, us_diagnosed_data = get_data("美国.txt", "jsonp_1629344292311_69436(", 2)
jp, jp_update_date, jp_diagnosed_data = get_data("日本.txt", "jsonp_1629350871167_29498(", 2)
ia, ia_update_date, ia_diagnosed_data = get_data("印度.txt", "jsonp_1629350745930_63180(", 2)

line = Line()

line.add_xaxis(us_update_date)

line.add_yaxis("美国确诊人数", us_diagnosed_data, label_opts=LabelOpts(is_show=False))
line.add_yaxis("日本确诊人数", jp_diagnosed_data, label_opts=LabelOpts(is_show=False))
line.add_yaxis("印度确诊人数", ia_diagnosed_data, label_opts=LabelOpts(is_show=False))

# 设置全局选项
line.set_global_opts(
    title_opts=TitleOpts(title="2020年 美日印三国确诊人数对比", pos_left="center", pos_bottom="1%"),
)

line.render()
print("图表生成成功！")
