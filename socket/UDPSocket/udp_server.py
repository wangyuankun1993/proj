# -*- coding: utf-8 -*-
# Product Name: PyCharm
# Project Name: wangyuankun
# File Name: udp_server
# Date: 2022/01/05 11:04:36
# Author: wangyuankun
# Function: This file is to achieve udp server!
# 导入socket模块
import socket

# 创建UDP套接字
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# 绑定地址到套接字
s.bind(('127.0.0.1',8888))

print("绑定UDP到8888端口")

# 接收数据
data,addr = s.recvfrom(1024)

# 转换公式
data = float(data) * 1.8 + 32

send_data = '转换后的温度（单位：华氏温度）：' + str(data)

# 发送给客户端
s.sendto(send_data.encode(), addr)

# 关闭服务器端套接字
s.close()

