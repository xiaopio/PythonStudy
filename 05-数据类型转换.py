# 将数字转换为字符串
num_str = str(11)
# <class 'str'>
print(type(num_str), num_str)

float_str = str(1.1)
print(type(float_str), float_str)

# 将字符串转换为数字
num1 = int("11")
print(type(num1), num1)

num2 = float("11.1")
print(type(num2), num2)

# 错误示例
# num3 = int("你好")
# Traceback ValueError: invalid literal for int() with base 10: '你好'
# print(type(num3), num3)

# 整数转浮点数
float_num = float(11)
# <class 'float'> 11.0
print(type(float_num), float_num)

# 浮点数转整数
int_num = int(1.1)
# <class 'int'> 1
print(type(int_num), int_num)
