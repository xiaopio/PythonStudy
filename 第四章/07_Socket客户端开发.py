# _*_ encoding: utf-8 _*_
"""
PyCharm 07_Socket客户端开发
2025年07月19日 10时23分56秒
by LiXiaoYang
"""

import socket

socket_client = socket.socket()

socket_client.connect(("localhost", 8888))

while True:
    msg = input("请输入要发送的消息:")
    if msg == 'exit':
        break
    socket_client.send(msg.encode("UTF-8"))
    recv = socket_client.recv(1024)
    print(f"服务器返回消息:{recv.decode('UTF-8')}")
socket_client.close()
