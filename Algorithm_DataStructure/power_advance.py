# -*- coding:utf-8 -*-
# Product Name: PyCharm
# Project Name: proj
# File Name: power_advance.py
# Date: 2022/02/02 00:36:20
# Author: wangyuankun
# Function: This file is to achieve xxx function!
def power(x, n):
    if n == 0:
        return 1
    else:
        partial = power(x, n // 2)
        result = partial * partial
        if n % 2 == 1:
            result *= x
        return result

print(power(2, 10))
