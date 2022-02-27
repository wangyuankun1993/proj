# -*- coding:utf-8 -*-
# Product Name: PyCharm
# Project Name: proj
# File Name: yield.py
# Date: 2022/01/31 10:42:36
# Author: wangyuankun
# Function: This file is to achieve xxx function!
def factors(n):
    k = 1
    while k * k < n:
        if n % k == 0:
            yield k
            yield n // k
        k += 1
    if k * k == n:
        yield k
