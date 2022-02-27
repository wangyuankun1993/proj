# -*- coding: utf-8 -*-
# Product Name: PyCharm
# Project Name: MySQL
# File Name: Chat_client
# Date: 2022/01/04 22:55:31
# Author: wangyuankun
# Function: This file is to achieve chat client!
# 导入socket模块
import socket

# 创建套接字
s = socket.socket()

# 获取主机地址
host = socket.gethostname()

# 设置端口号
port = 12345

# 主动初始化TCP服务器连接
s.connect((host,port))

print("已连接")

info = ""

# 判断是否退出
while info != 'byebye':
    # 输入内容
    send_data = input("输入发送内容：")
    # 发送TCP数据
    s.send(send_data.encode())
    # 判断是否退出
    if send_data == 'byebye':
        break
    # 接收服务器数据
    info = s.recv(1024).decode()
    print("接收到的内容为：", info)
# 关闭套接字
s.close()