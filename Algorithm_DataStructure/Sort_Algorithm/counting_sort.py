# -*- coding:utf-8 -*-
# Product Name: PyCharm
# Project Name: proj
# File Name: counting_sort.py
# Date: 2022/02/11 15:39:43
# Author: wangyuankun
# Function: This file is to achieve xxx function!
def counting_sort(d0):
    d_max = 0
    d_min = 0
    for i in d0:
        if d_max < i:
            d_max = i
        if d_min > i:
            d_min = i
    d1 = {}
    for i in d0:
        if i in d1.keys():
            d1[i] += 1
        else:
            d1[i] = 1
    d2 = []
    for i in range(d_min, d_max + 1):
        if i in d1.keys():
            for j in range(d1[i]):
                d2.append(i)
    print(d2)

d0 = [2, 15, 5, 9, 7, 6, 4, 12, 5, 4, 2, 64, 5, 6, 4, 2, 3, 54, 45, 4, 44]
d1 = counting_sort(d0)
