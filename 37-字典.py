# _*_ encoding: utf-8 _*_
"""
PyCharm 37-字典
2025年07月14日 21时36分04秒
by LiXiaoYang
"""

my_dict1 = {"张三": 99, "周杰伦": 88, "林俊杰": 77}

my_dict2 = {}

my_dict3 = dict()

# 字典1的内容是：{'张三': 99, '周杰伦': 88, '林俊杰': 77}，类型<class 'dict'>
print(f"字典1的内容是：{my_dict1}，类型{type(my_dict1)}")
# 字典2的内容是：{}，类型<class 'dict'>
print(f"字典2的内容是：{my_dict2}，类型{type(my_dict2)}")
# 字典3的内容是：{}，类型<class 'dict'>
print(f"字典3的内容是：{my_dict3}，类型{type(my_dict3)}")

zhou_score = my_dict1["周杰伦"]

print(zhou_score)

# 定义嵌套字典
stu_score_dict = {
    "王力宏": {
        "chinese": 77,
        "math": 66,
        "english": 33,
    },
    "周杰伦": {
        "chinese": 88,
        "math": 86,
        "english": 55,
    },
    "林俊杰": {
        "chinese": 99,
        "math": 96,
        "english": 66,
    },
}

# 看周杰伦的语文信息

zhou_chinese = stu_score_dict.get("周杰伦").get("chinese")
# None
zhou_jp = stu_score_dict.get("周杰伦").get("jp")
# KeyError 报错信息
# zhou_jp = stu_score_dict["周杰伦"]["jp"]

print(zhou_chinese)

print(zhou_jp)

# 新增元素

stu_score_dict["张信哲"] = {
    "chinese": 66,
    "math": 66,
    "english": 33,
}
print(stu_score_dict)

# 修改元素

stu_score_dict["周杰伦"]["chinese"] = 99
print(stu_score_dict)

# 移除一个元素

zhou_score = stu_score_dict.pop("周杰伦")
print(stu_score_dict)
print(zhou_score)

# 获取全部key

keys = stu_score_dict.keys()
print(keys)

# 遍历字典
for key in keys:
    print(f"key:{key}, value:{stu_score_dict[key]}")

for key in stu_score_dict:
    print(f"key:{key}, value:{stu_score_dict[key]}")

# 清空元素


stu_score_dict.clear()
print(stu_score_dict)

employee_info_dict = {
    "王力宏": {
        "department": "科技部",
        "salary": 3000,
        "level": 1
    },
    "周杰伦": {
        "department": "市场部",
        "salary": 5000,
        "level": 2
    },
    "林俊杰": {
        "department": "市场部",
        "salary": 7000,
        "level": 3
    },
    "张学友": {
        "department": "科技部",
        "salary": 4000,
        "level": 1
    },
    "刘德华": {
        "department": "市场部",
        "salary": 6000,
        "level": 2
    },
}
print(employee_info_dict)

for name in employee_info_dict:
    if employee_info_dict[name]["level"] == 1:
        employee_info_dict[name]["level"] = 2
        employee_info_dict[name]["salary"] += 1000
print(employee_info_dict)
