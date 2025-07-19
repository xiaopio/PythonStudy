# _*_ encoding: utf-8 _*_
"""
PyCharm 05_多线程编程
2025年07月19日 09时37分10秒
by LiXiaoYang
"""
import time
import threading


def sing(msg):
    while True:
        print(f"我在{msg}......")
        time.sleep(1)


def dance(msg):
    while True:
        print(f"我在{msg}......")
        time.sleep(1)


if __name__ == '__main__':
    # 单线程演示
    # 只会唱歌，跳舞不会执行
    #     sing()
    #     dance()
    # 创建线程
    # 元组形式传参
    sing_thread = threading.Thread(target=sing, args=("唱歌",))
    # 字典形式传参
    dance_thread = threading.Thread(target=dance, kwargs={"msg": "跳舞"})
    # 启动线程
    sing_thread.start()
    dance_thread.start()
