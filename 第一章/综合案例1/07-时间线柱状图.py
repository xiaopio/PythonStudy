# _*_ encoding: utf-8 _*_
"""
PyCharm 07-时间线柱状图
2025年07月16日 14时41分50秒
by LiXiaoYang
"""

from pyecharts.charts import Bar, Timeline
from pyecharts.options import LabelOpts
from pyecharts.globals import ThemeType

bar1 = Bar()
bar1.add_xaxis(["中国", "美国", "英国"])
bar1.add_yaxis("GDP", [30, 30, 20], label_opts=LabelOpts(position="right"))
# 反转柱状图
bar1.reversal_axis()

bar2 = Bar()
bar2.add_xaxis(["中国", "美国", "英国"])
bar2.add_yaxis("GDP", [70, 60, 10], label_opts=LabelOpts(position="right"))
# 反转柱状图
bar2.reversal_axis()

bar3 = Bar()
bar3.add_xaxis(["中国", "美国", "英国"])
bar3.add_yaxis("GDP", [140, 120, 30], label_opts=LabelOpts(position="right"))
# 反转柱状图
bar3.reversal_axis()


# 构建时间线对象
# 设置主题
timeline = Timeline({"theme": ThemeType.LIGHT})

# 添加时间线
timeline.add(bar1, "点1")
timeline.add(bar2, "点2")
timeline.add(bar3, "点3")

# 自动播放设置
timeline.add_schema(
    play_interval=1000,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=True,
)

# 绘图
timeline.render("基础时间线柱状图.html")


