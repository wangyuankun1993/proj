# -*- coding:utf-8 -*-
# Product Name: PyCharm
# Project Name: proj
# File Name: power.py
# Date: 2022/02/02 00:24:32
# Author: wangyuankun
# Function: This file is to achieve xxx function!d
def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)

print(power(3, 4))
