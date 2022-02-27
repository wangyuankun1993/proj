# -*- coding: utf-8 -*-
# Product Name: PyCharm
# Project Name: PycharmProjects
# File Name: client
# Date: 2021/12/05 15:33:02
# Author: wangyuankun
# Function: This file is to achieve client!

# 导入socket、sys模块
import socket
import sys

# 创建socket对象
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 获取本地主机名
host = socket.gethostname()

# 设置端口号
port = 10000

# 连接服务，指定主机和端口
s.connect((host, port))

while True:
    # 提示用户输入输入数据
    send_data = input("请输入要发送的数据：")
    s.send(send_data.encode('utf-8'))

    # 接收对方发送过来的数据，最大接收1024字节
    msg = s.recv(1024).decode('utf-8')
    print("接收到的数据为：", msg)

# 关闭套接字
# s.close()
