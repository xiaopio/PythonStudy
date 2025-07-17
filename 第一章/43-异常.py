# _*_ encoding: utf-8 _*_
"""
PyCharm 43-异常
2025年07月15日 10时39分57秒
by LiXiaoYang
"""

# try:
#     f = open("D:/abc.txt", "r", encoding="utf-8")
# except:
#     print("出现异常了，文件不存在，将r模式改为w模式")
#     f = open("D:/abc.txt", "w", encoding="utf-8")
#     print("创建文件成功!")

# f.close()

# 捕获指定的异常
# try:
#     print(name)
# # 捕获指定类型的异常，其他类型的异常不会被捕获，还是会报错
# except NameError as e:
#     print(f"出现了变量未定义的异常，异常提示信息：{e}")

# 捕获多个的异常
# try:
#     # print(name)
#     print(1 / 0)
#     # 捕获指定类型的异常，其他类型的异常不会被捕获，还是会报错
# except (NameError, ZeroDivisionError) as e:
#     print(f"异常提示信息：{e}")

# 捕获所有异常
# try:
#     print()
#     # print(name)
#     # print(1 / 0)
# except Exception as e:
#     print(e)
# else:
#     print("没有出现异常的操作")
# finally:
#     print("有没有异常都要执行")


# 异常具有传递性
def func1():
    print("f1开始执行")
    print(1 / 0)
    print("f1结束执行")

def func2():
    print("f2开始执行")
    func1()
    print("f2结束执行")

def main():
    try:
        print("main开始执行")
        func2()
        print("main结束执行")
    except Exception as e:
        print(f"异常提示信息:{e}")
    else:
        print("没有异常的操作")
    finally:
        print("有没有异常都执行")
main()