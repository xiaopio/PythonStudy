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

for i in range(5, 10):
    print(f"{i}\t", end='')
print()

for i in range(5, 10, 2):
    print(f"{i}\t", end='')
print()

num = 100
count2 = 0
for i in range(1, num + 1):
    if i % 2 == 0:
        count2 += 1
print(f"1到{num}之间一共有{count2}个偶数")
print(i)


