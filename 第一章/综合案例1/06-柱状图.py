# _*_ encoding: utf-8 _*_
"""
PyCharm 06-动态柱状图
2025年07月16日 10时53分51秒
by LiXiaoYang
"""
from pyecharts.charts import Bar
from pyecharts.options import LabelOpts

bar = Bar()

bar.add_xaxis(["中国", "美国", "英国"])
bar.add_yaxis("GDP", [30, 20, 10], label_opts=LabelOpts(position="right"))

# 反转柱状图
bar.reversal_axis()
bar.render("基础柱状图.html")

