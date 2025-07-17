# _*_ encoding: utf-8 _*_
"""
PyCharm 06-河南省疫情地图
2025年07月16日 09时41分09秒
by LiXiaoYang
"""
from get_data_module import get_provincial_confirmed_data
from pyecharts.charts import Map
from pyecharts import options as opts

[
    ('台湾', 0), ('江苏', 1), ('云南', 2), ('河南', 3), ('上海', 4), ('湖南', 5), ('湖北', 6), ('广东', 7), ('香港', 8),
    ('福建', 9), ('浙江', 10), ('山东', 11),
    ('四川', 12), ('天津', 13), ('北京', 14), ('陕西', 15), ('广西', 16), ('辽宁', 17), ('重庆', 18), ('澳门', 19),
    ('甘肃', 20), ('山西', 21), ('海南', 22),
    ('内蒙古', 23), ('吉林', 24), ('黑龙江', 25), ('宁夏', 26), ('青海', 27), ('江西', 28), ('贵州', 29), ('西藏', 30),
    ('安徽', 31), ('河北', 32), ('新疆', 33)
]
province_name, data = get_provincial_confirmed_data("疫情.txt", 11)

# print(province_name, data)

map = Map()

# 全局选项
map.add(province_name + "疫情数据分布", data, province_name).set_global_opts(
    title_opts=opts.TitleOpts(title=f"{province_name}疫情地图", subtitle="数据示例"),
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
).render(f"{province_name}疫情数据.html")

print(f"地图已生成并保存为 {province_name}疫情数据.html，请在浏览器中打开查看")
