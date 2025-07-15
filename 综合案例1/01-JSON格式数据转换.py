# _*_ encoding: utf-8 _*_
"""
PyCharm 01-JSON格式数据转换
2025年07月15日 15时50分59秒
by LiXiaoYang
"""
import json

data = [{"name": "张三", "age": 13}, {"name": "李四", "age": 14}, {"name": "王五", "age": 15}]
json_str = json.dumps(data, ensure_ascii=False)
# ensure_ascii=True
# [{"name": "\u5f20\u4e09", "age": 13}, {"name": "\u674e\u56db", "age": 14}, {"name": "\u738b\u4e94", "age": 15}]
# ensure_ascii=False
# [{"name": "张三", "age": 13}, {"name": "李四", "age": 14}, {"name": "王五", "age": 15}] <class 'str'>
print(json_str, type(json_str))

stu = {"name": "周杰伦", "age": 13}
json_stu = json.dumps(stu, ensure_ascii=False)
# {"name": "周杰伦", "age": 13} <class 'str'>
print(json_stu, type(json_stu))

s = '[{"name": "张三", "age": 13}, {"name": "李四", "age": 14}, {"name": "王五", "age": 15}]'

l = json.loads(s)
# [{'name': '张三', 'age': 13}, {'name': '李四', 'age': 14}, {'name': '王五', 'age': 15}] <class 'list'>
print(l, type(l))

s = '{"name": "周杰伦", "age": 13}'
d = json.loads(s)
# {'name': '周杰伦', 'age': 13} <class 'dict'>
print(d, type(d))
