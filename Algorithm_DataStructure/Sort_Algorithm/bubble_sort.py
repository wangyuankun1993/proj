# -*- coding:utf-8 -*-
# Product Name: PyCharm
# Project Name: proj
# File Name: bubble_sort.py
# Date: 2022/02/10 10:34:31
# Author: wangyuankun
# Function: This file is to achieve xxx function!
def bubble_sort():
    d0 = [2, 15, 5, 9, 7, 6, 4, 12, 5, 4, 2, 64, 5, 6, 4, 2, 3, 54, 45, 4, 44]
    while True:
        state = 0 # first loop
        for i in range(len(d0) - 1):
            if d0[i] > d0[i + 1]:
                d0[i], d0[i + 1] = d0[i + 1], d0[i]
                state = 1
        if not state:
            break
    return d0

a = bubble_sort()
print(a)
