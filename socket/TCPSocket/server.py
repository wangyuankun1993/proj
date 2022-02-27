# -*- coding: utf-8 -*-
# Product Name: PyCharm
# Project Name: PycharmProjects
# File Name: server
# Date: 2021/12/05 11:35:29
# Author: wangyuankun
# Function: This file is to achieve server!

# 导入socket、sys模块
import socket
import sys

# 创建socket对象
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 获取本地主机名
host = socket.gethostname()
print(host)

port = 10000

# 绑定端口号
serversocket.bind((host, port))

# 等待客户端连接
print("服务器等待客户端连接...")

# 设置最大连接数，超过后排队
serversocket.listen(5)

while True:
    # 建立客户端连接
    clientsocket,addr = serversocket.accept()
    data = clientsocket.recv(1024)
    print(data)
    print("链接地址：%s" % str(addr))
    msg = '相信你们白头偕老，永结同心！' + "\r\n"
    clientsocket.send(msg.encode('utf-8'))
    clientsocket.close()