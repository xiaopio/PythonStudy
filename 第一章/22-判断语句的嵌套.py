# if int(input("请输入您的身高(单位cm):")) > 120:
#     if int(input("请输入您的年龄:")) < 10:
#         print("未满10周岁，无需购票")
#     else:
#         print("您已满10周岁，且身高超出限制，请支付10元票价。")
# else:
#     print("身高未超出限制，可以免费游玩")

age = int(input("请输入你的年龄:"))

onboarding_time = int(input("请输入你的入职时间:"))

level = int(input("请输入你的级别:"))

if 30 > age >= 18:
    if onboarding_time > 2:
        print("可以领取礼物。")
    elif level > 3:
        print("可以领取礼物。")
    else:
        print("你的入职时间不足两年or等级小于3级，不能领取礼物。")
else:
    print("您的年龄大于30岁或小于18岁，不能领取礼物")

