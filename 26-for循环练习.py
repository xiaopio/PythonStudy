# 100天，每天送10朵花，表白一次
i = 0
for i in range(100):
    print(f"今天是向小美表白的第{i + 1}天，加油坚持。")
    for j in range(10):
        print(f"向小美送的第{j + 1}朵花。")
    print("小美，我喜欢你。")
print(f"表白了{i + 1}天，表白成功。")

# 99乘法表

for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j} * {i} = {j * i}\t", end='')
    print()


def bubble_sort(arr):
    """
    冒泡排序
    :param arr: 数组
    :return: 排序好的数组
    """
    n = len(arr)
    # 遍历所有数组元素
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # 遍历数组中的每个元素，比较并交换顺序
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


arr1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
bubble_sort()
print(arr1)
