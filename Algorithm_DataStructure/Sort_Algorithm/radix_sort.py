# -*- coding:utf-8 -*-
# Product Name: PyCharm
# Project Name: proj
# File Name: radix_sort.py
# Date: 2022/02/11 17:32:53
# Author: wangyuankun
# Function: This file is to achieve xxx function!
def radix_sort(d0):
    d1 = [[] for x in range(10)]

    for i in d0:
        d1[i % 10].append(i)
    print(d1)

    d0_1 = []
    for i in d1:
        if i:
            for j in i:
                d0_1.append(j)
    print(d0_1)

    d2 = [[] for x in range(10)]
    for i in d0_1:
        d2[int(i/10)].append(i)
    print(d2)

    d0_2 = []
    for i in d0_2:
        for j in i:
            d0_2.append(j)
    print(d0_2)

d0 = [2, 15, 5, 9, 7, 6, 4, 12, 5, 4, 2, 64, 5, 6, 4, 2, 3, 54, 45, 4, 44]
radix_sort(d0)
