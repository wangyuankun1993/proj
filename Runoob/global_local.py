# -*- coding:utf-8 -*-
# Product Name: PyCharm
# Project Name: proj
# File Name: global_local.py
# Date: 2022/01/27 17:10:15
# Author: wangyuankun
# Function: This file is to achieve xxx function!
total = 0
def sum(arg1, arg2):
    total = arg1 + arg2
    print("Local variable: ", total)
    return total

sum(10, 20)
print("Golbal variable: ", total)
