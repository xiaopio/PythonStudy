# _*_ encoding: utf-8 _*_
"""
PyCharm 02-pyecharts
2025年07月15日 17时24分10秒
by LiXiaoYang
"""
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, VisualMapOpts
# 创建一个折线图对象
line = Line()
# 添加x轴数组
line.add_xaxis(["中国", "美国", "英国"])
# 添加y轴数据
line.add_yaxis("GDP", [30, 20, 10])

# 设置全局配置
line.set_global_opts(
    title_opts=TitleOpts(title="GDP展示", pos_left="50%", pos_bottom="1%"),
    legend_opts=LegendOpts(is_show=True),
    toolbox_opts=ToolboxOpts(is_show=True),
    visualmap_opts=VisualMapOpts(is_show=True),
)

# 通过render方法生成图像
line.render()
