# -*- coding:utf-8 -*-
# Product Name: PyCharm
# Project Name: proj
# File Name: recursion.py
# Date: 2022/02/13 16:52:49
# Author: wangyuankun
# Function: This file is to achieve xxx function!
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

a = fact(100)
print(a)
