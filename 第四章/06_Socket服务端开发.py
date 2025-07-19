# _*_ encoding: utf-8 _*_
"""
PyCharm 06_Socket服务端开发
2025年07月19日 09时50分22秒
by LiXiaoYang
"""

import socket

# 创建socket对象
socket_server = socket.socket()
# 绑定ip和端口
socket_server.bind(("localhost", 8888))
# 监听端口
# listen方法内接收一个整数参数，表示接受的连接数量
socket_server.listen(1)
# 等待客户端连接
# result = socket_server.accept()
# conn = result[0]  # 客户端和服务端的连接对象
# address = result[1]  # 客户端的地址信息
# accept()方法是阻塞的方法，没有客户端连接，代码就不会继续往下执行
conn, address = socket_server.accept()
print(f"接收到了客户端信息，{conn, address}")

while True:
    # 接收客户端信息 要使用客户端和服务端本次链接对象，而非socket_server对象
    # recv接收的参数是缓冲区大小
    # recv方法的返回值是一个字节数组也就是bytes对象,不是字符串,可以通过decode方法通过UTF-8编码,将字节数组转换为字符串数组
    data: str = conn.recv(1024).decode("UTF-8")
    print(f"客户端发来的消息是:{data}")
    # 发送回复消息
    msg = input("请输入你要给客户端回复的消息:")
    if msg == "exit":
        break

    conn.send(msg.encode("UTF-8"))  # encode将字符串编码为字节数组
# 关闭连接
conn.close()
socket_server.close()
