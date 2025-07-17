# _*_ encoding: utf-8 _*_
"""
PyCharm 05-全国疫情地图构建
2025年07月15日 21时21分14秒
by LiXiaoYang
"""
from pyecharts.charts import Map
from pyecharts import options as opts
from get_data_module import get_provinces_diagnosed_data as get_data

data = get_data("疫情.txt")

# 创建地图对象并设置宽度和高度
(
    Map(init_opts=opts.InitOpts(
        width="1000px",  # 地图宽度 - 可根据需要调整
        height="800px",  # 地图高度 - 可根据需要调整
        # theme=ThemeType.LIGHT  # 设置主题
    ))
    .add("各省份确诊人数", data, "china")
    .set_global_opts(
        title_opts=opts.TitleOpts(title="全国疫情地图", subtitle="数据示例"),
        visualmap_opts=opts.VisualMapOpts(
            is_show=True,
            is_piecewise=True,
            pieces=[
                {"min": 1, "max": 9, "label": "1-9人", "color": "#CCFFFF"},
                {"min": 10, "max": 99, "label": "10-99人", "color": "#FFFF99"},
                {"min": 100, "max": 999, "label": "100-999人", "color": "#FF9966"},
                {"min": 1000, "max": 9999, "label": "1000-9999人", "color": "#FF6666"},
                {"min": 10000, "max": 99999, "label": "10000-99999人", "color": "#CC3333"},
                {"min": 100000, "label": "100000人以上", "color": "#990033"},
            ]
        ),
        toolbox_opts=opts.ToolboxOpts(is_show=True)  # 显示工具箱
    )
    .render("china_map.html")  # 生成 HTML 文件
)

print("地图已生成并保存为 map.html，请在浏览器中打开查看")
