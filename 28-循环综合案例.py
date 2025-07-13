# _*_ encoding: utf-8 _*_
"""
PyCharm 28-循环综合案例
2025年07月13日 19时33分08秒
by LiXiaoYang
"""
import random

balance = 10000
employees_num = 20
limit_point = 5
for i in range(employees_num):
    if balance == 0:
        print("工资发放完了，下个月领取吧。")
        break
    else:
        performance_score = random.randint(1, 10)
        if performance_score < limit_point:
            print(f"员工{i + 1}，绩效分{performance_score}，低于{limit_point}，不发工资，下一位。")
            continue
        else:
            balance -= 1000
            print(f"员工{i + 1}，绩效分{performance_score}，发放工资1000元，账户余额还剩{balance}元")
