# -*- coding:utf-8 -*-
# Product Name: PyCharm
# Project Name: proj
# File Name: binary_sum.py
# Date: 2022/02/02 00:49:36
# Author: wangyuankun
# Function: This file is to achieve xxx function!
def binary_sum(S, start, stop):
    if start >= stop:
        return 0
    elif start == stop - 1:
        return S[start]
    else:
        mid = (start + stop) / 2
        return binary_sum(S, start, mid) + binary_sum(S, mid, stop)

print(binary_sum([1,3,4,5], 0 ,3))
