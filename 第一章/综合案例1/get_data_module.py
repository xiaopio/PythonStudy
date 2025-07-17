# _*_ encoding: utf-8 _*_
"""
PyCharm get_data_module
2025年07月15日 17时55分44秒
by LiXiaoYang
"""

import json


def get_diagnosed_data(file_name: str, begin_to_remove_str: str, end_to_remove_num: int):
    """
    获取国外疫情数据
    :param file_name: 文件地址
    :param begin_to_remove_str: 移除的前几位非JSON格式字符串
    :param end_to_remove_num: 移除后几位
    :return: country_name 国家名, update_date 更新日期, diagnosed_data 确诊人数
    """
    _f = None
    try:
        _f = open(file_name, "r", encoding="utf-8")
        _data = _f.read()
        _data = _data.replace(begin_to_remove_str, "")
        _data = _data[:-end_to_remove_num]
        _dict = json.loads(_data)
        country_name = _dict['data'][0]['name']
        update_date = _dict['data'][0]['trend']['updateDate'][:314]
        diagnosed_data = _dict['data'][0]['trend']['list'][0]['data'][:314]

    except Exception as e:
        print(f"打开文件失败，错误信息：{e}")

    finally:
        if _f:
            _f.close()
    return country_name, update_date, diagnosed_data


def add_suffix_to_the_province_name(_provinces_name_list: list):
    """
    将省份名加上后缀
    :param _provinces_name_list: 省份名列表
    :return: 加后缀的省份名
    """
    # 定义省份后缀映射
    municipality = {"北京", "天津", "上海", "重庆"}  # 直辖市
    autonomous_region = {"内蒙古", "西藏"}  # 自治区
    ss_region = {"新疆"}  # 新疆维吾尔自治区
    sss_region = {"广西"}  # 广西壮族自治区
    ssss_region = {"宁夏"}
    special_admin = {"香港", "澳门"}  # 特别行政区
    provinces_name = []
    for name in _provinces_name_list:
        if name in municipality:
            provinces_name.append(f"{name}市")
        elif name in autonomous_region:
            provinces_name.append(f"{name}自治区")
        elif name in ss_region:
            provinces_name.append(f"{name}维吾尔自治区")
        elif name in sss_region:
            provinces_name.append(f"{name}壮族自治区")
        elif name in ssss_region:
            provinces_name.append(f"{name}回族自治区")
        elif name in special_admin:
            provinces_name.append(f"{name}特别行政区")
        else:
            provinces_name.append(f"{name}省")  # 默认为省
    return provinces_name


def get_provinces_diagnosed_data(file_name: str, ):
    """
    获取国内各省份疫情确诊人数
    :param file_name: 数据文件地址
    :return: 各省份疫情确诊人数元组列表 [("province": num), ...]
    """
    _fr = None
    try:
        _fr = open(file_name, 'r', encoding='utf-8')
    except Exception as e:
        print(f"错误提示信息:{e}")
    else:
        _data = _fr.read()
        _data = json.loads(_data)
        areas = _data["areaTree"][0]["children"]
        provinces_name_list = []
        provinces_name_list.extend(area["name"] for area in areas)
        provinces_name = add_suffix_to_the_province_name(provinces_name_list)
        confirmed_num_list = []
        confirmed_num_list.extend(area["total"]["confirm"] for area in areas)
        if len(confirmed_num_list) == len(provinces_name):
            return list(zip(provinces_name, confirmed_num_list))
        else:
            raise ValueError("两个列表的长度必须相同")
    finally:
        if _fr:
            _fr.close()


def get_provincial_confirmed_data(file_name: str, city_num: int):
    """
    获取各省份确诊数据
    :param file_name: 文件路径
    :param city_num: 城市编号
    :return: province_name 省份名, data 城市确诊数据
    """
    _fr = None
    try:
        _fr = open(file_name, "r", encoding="utf-8")
    except Exception as e:
        print(f"错误提示:{e}")
    else:
        _data = _fr.read()
        _data = json.loads(_data)
        areas = _data["areaTree"][0]["children"][city_num]
        province_name = areas["name"]
        # province_name = add_suffix_to_the_province_name({areas["name"]})[0]
        data = []
        for city in areas["children"]:
            city_name = city["name"]
            # TODO 这里只对河南省名称不规范的地市进行了修改，其他省份，直辖市、自治州什么的没做优化
            if city_name == "济源示范区":
                city_name = city["name"][:-3] + "市"
            elif city_name == "地区待确认":
                city_name = city["name"]
            else:
                city_name = city["name"] + "市"
            confirmed_num = city["total"]["confirm"]
            data.append((city_name, confirmed_num))
        # print(data)
        return province_name, data
    finally:
        if _fr:
            _fr.close()

# get_provincial_confirmed_data

# if __name__ == '__main__':

#     country_name, update_date, diagnosed_data = get_diagnosed_data('美国.txt', 'jsonp_1629344292311_69436(', 2)
#     print(country_name, update_date, diagnosed_data)
#     data = get_provincial_confirmed_data()
#     print(data)
