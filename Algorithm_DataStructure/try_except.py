# -*- coding:utf-8 -*-
# Product Name: PyCharm
# Project Name: proj
# File Name: try_except.py
# Date: 2022/01/30 23:25:55
# Author: wangyuankun
# Function: This file is to achieve xxx function!
age = -1
while age <= 0:
    try:
        age = int(input("Please input age: "))
        if age <= 0:
            print("Your age must be a positive value.")
    except (ValueError, EOFError):
        pass
