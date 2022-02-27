# -*- coding:utf-8 -*-
# Product Name: PyCharm
# Project Name: proj
# File Name: factorial.py
# Date: 2022/02/01 18:25:21
# Author: wangyuankun
# Function: This file is to achieve xxx function!
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))
