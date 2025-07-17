# 单引号
name = '张三'
print(type(name), name)

# 双引号
name = "张三"
print(type(name), name)

# 三引号
name = """
张
三
"""
print(type(name), name)

# 字符串中包含双引号
name = '"张三"'
print(type(name), name)

# 字符串中包含单引号
name = "'张三'"
print(type(name), name)

# 只有一个引号，使用转义字符 \ 解除引号的效用
name = "\"张三"
print(type(name), name)
