name = "master"
for i in name:
    print(i)

# 统计一个字符串中有几个a
str = "This is an apple"
count = 0
for i in str:
    if i == "a":
        count += 1
print(f"一共有{count}个a")

# range(num1, num2, step) num1 开始、num2 结束、step 步长
for i in range(10):
    # 0 ~ 9
    print(f"{i}\t", end='')
print()

for j in range(5, 10):
    print(f"{j}\t", end='')
print()

for k in range(5, 10, 2):
    print(f"{k}\t", end='')

