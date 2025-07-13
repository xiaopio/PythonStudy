import random

num = random.randint(1, 10)
print(num)
i = 0
while i < 3:
    guess_number = int(input("请输入你猜测的数字:"))
    if guess_number == num:
        print("恭喜你，猜对啦。")
        break
    else:
        if guess_number > num:
            print("不对，大了。")
        else:
            print("不对，小了。")
    i += 1
