print("欢迎来到嘿嘿动物园。")
height = int(input("请输入您的身高(cm):"))
height_limit = 120
if height > height_limit:
    print("您的身高超出120cm，游玩需要购票10元。")
else:
    print("您的身高未超出120cm，可以免费游玩。")

print("祝您游玩愉快。")
