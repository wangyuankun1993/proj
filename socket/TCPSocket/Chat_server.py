# -*- coding: utf-8 -*-
# Product Name: PyCharm
# Project Name: MySQL
# File Name: Chat_server
# Date: 2022/01/04 22:56:05
# Author: wangyuankun
# Function: This file is to achieve chat server!
# 导入socket模块
import socket

# 获取主机地址
host = socket.gethostname()

# 设置端口号
port = 12345

# 创建套接字
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 绑定地址到套接字
s.bind((host,port))

# 设置最多连接数量
s.listen(1)

# 被动接受TCP客户端连接
sock,addr = s.accept()

print("连接已经建立")

# 接收客户端数据
info = sock.recv(1024).decode()

while info != 'byebye':
    if info:
        print("接收到的内容：", info)
    # 发送消息
    send_data = input("输入发送内容：")
    # 发送TCP数据
    sock.send(send_data.encode())
    if send_data == 'byebye':
        break
    # 接收客户端数据
    info = sock.recv(1024).decode()
# 关闭客户端套接字
sock.close()
# 关闭服务器套接字
s.close()