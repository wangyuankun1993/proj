# -*- coding: utf-8 -*-
# Product Name: PyCharm
# Project Name: wangyuankun
# File Name: udp_client
# Date: 2022/01/05 11:32:35
# Author: wangyuankun
# Function: This file is to achieve udp client!
# 导入socket模块
import socket

# 创建UDP套接字
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# 输入要转换的温度
data = input("请输入要转换的温度（单位：摄氏温度）：")

# 发送数据
s.sendto(data.encode(),('127.0.0.1',8888))

# 打印接收到的数据
print(s.recv(1024).decode())

# 关闭套接字
s.close()
