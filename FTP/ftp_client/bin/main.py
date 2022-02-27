# -*- coding: utf-8 -*-
# Product Name: PyCharm
# Project Name: wangyuankun
# File Name: main.py
# Date: 2021/6/14 14:34:02
# Author: wangyuankun
# Function: This file is to achieve program entrance !
import os, sys

# 获取当前文件的上两级目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from core.client import FtpClient

if __name__ == '__main__':
    ftp = FtpClient()
    ftp.connect('localhost', 9999)

    auth_tag = False
    count = 0
    while auth_tag != True: # 功能：3次验证不通过即退出
        count += 1
        if count <= 3:
            auth_tag = ftp.auth()
        else:
            exit()

    ftp.interactive()
    ftp.close()