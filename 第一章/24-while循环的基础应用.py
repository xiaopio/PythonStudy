# import random

# i = 0
# while i < 100:
#     print(f"第{i + 1}次")
#     i += 1

# count = 1
# sum = 0
# while count <= 100:
#     sum += count
#     # print(i)
#     count += 1
# print(sum)

# num = random.randint(1, 100)
# print(num)
# count = 0
# flag = True
# while flag:
#     count += 1
#     guess_number = int(input("请输入你猜测的数字:"))
#     if num == guess_number:
#         print(f"恭喜你，猜对啦，一共猜了{count}次。")
#         flag = False
#     elif guess_number > num:
#         print("不对，大了")
#     else:
#         print("不对，小了")

# 100天，每天送10朵花，表白一次
# i = 1
# while i <= 100:
#     print(f"今天是第{i}天，准备表白......")
#     j = 1
#     while j <= 10:
#         print(f"送给小美的第{j}朵花")
#         j += 1
#     print(f"喜欢小美的第{i}天，小美我喜欢你")
#     i += 1
# print(f"坚持了{i - 1}天，表白成功。")

# 99乘法表
i = 1
while i < 10:
    j = 1
    while j <= i:
        print(f"{j} * {i} = {j*i}\t", end="")
        j += 1
    print()
    i += 1
