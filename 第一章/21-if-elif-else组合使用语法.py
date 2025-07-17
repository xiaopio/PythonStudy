# grades = float(input("请输入你的成绩:"))
#
# if grades >= 90:
#     print("优秀")
# elif grades >= 80:
#     print("良好")
# elif grades >= 70:
#     print("中等")
# elif grades >= 60:
#     print("及格")
# else:
#     print("不及格")

number = 10

if int(input("请输入第一次猜想的数字:")) == number:
    print("猜对啦")
elif int(input("不对，请再猜一次:")) == number:
    print("猜对啦")
elif int(input("不对再猜最后一次:")) == number:
    print("猜对啦")
else:
    print(f"Sorry，全部猜错啦，我想的是：{number}")
