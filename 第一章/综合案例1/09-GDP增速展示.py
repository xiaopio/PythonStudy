# _*_ encoding: utf-8 _*_
"""
PyCharm 09-GDP增速展示
2025年07月16日 15时05分16秒
by LiXiaoYang
"""
from pyecharts.charts import Bar, Timeline, Grid
from pyecharts.globals import ThemeType
from pyecharts.options import LabelOpts, GraphicShapeOpts, GraphicTextStyleOpts, TitleOpts, ToolboxOpts, GraphicText, \
    GraphicGroup

timeline = Timeline({"theme": ThemeType.LIGHT})

_f = None
try:
    _f = open('1960-2019全球GDP数据.csv', 'r', encoding='GB2312')
except Exception as e:
    print(f"错误信息:{e}")
else:
    data_lines = _f.readlines()
    data_lines.pop(0)
    #     key: 年份, value: 国家及GDP
    data_dict = {}
    for line in data_lines:
        year = int(line.split(",")[0])
        country = line.split(",")[1]
        gdp = float(line.split(",")[2])
        try:
            data_dict[year].append([country, gdp])
        except KeyError:
            data_dict[year] = []
            data_dict[year].append([country, gdp])
    # print(data_dict)
finally:
    if _f:
        _f.close()
sorted_year_list = sorted(data_dict.keys())
# print(sorted_year_list)
for year in sorted_year_list:
    data_dict[year].sort(key= lambda element: element[1], reverse=True)
    # 取出本年份前8名的国家
    year_data = data_dict[year][0:8]
    x_data = []
    y_data = []
    for country_gdp in year_data:
        x_data.append(country_gdp[0])
        y_data.append(country_gdp[1] / 100000000)
    x_data.reverse()
    y_data.reverse()
    # 构建柱状图
    bar = Bar()
    bar.add_xaxis(x_data)
    bar.add_yaxis("GDP(亿)", y_data, label_opts=LabelOpts(position="right"))
    # 添加时间线
    timeline.add(bar, year)
    # 反转x轴和y轴
    bar.reversal_axis()
    bar.set_global_opts(
        title_opts=TitleOpts(title="全球GDP前8名国家", subtitle=f"{year}年"),
        xaxis_opts={"name": "GDP(亿)"},
        yaxis_opts={"name": "国家"},
    )
    timeline.add(bar, str(year))

# 自动播放设置
timeline.add_schema(
    play_interval=300,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=True,
)

# 绘图
timeline.render("全球GDP增长柱状图.html")
print("已生成并保存为 全球GDP增长柱状图.html，请在浏览器中打开查看")
