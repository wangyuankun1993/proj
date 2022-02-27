# -*- coding:utf-8 -*-
# Product Name: PyCharm
# Project Name: proj
# File Name: bucket_sort.py
# Date: 2022/02/11 16:01:54
# Author: wangyuankun
# Function: This file is to achieve xxx function!
def bucket_sort(d0):
    d1 = [[] for x in range(10)]
    for i in d0:
        d1[int(i/10)].append(i)

    for i in range(len(d1)):
        if d1[i] != []:
            d2 = [[] for x in range(10)]
            for j in d1[i]:
                d2[j%10].append(j)
            d1[i] = d2

    d3 = []
    for i in d1:
        if i:
            for j in i:
                if j:
                    for k in j:
                        if k:
                            d3.append(k)
    print(d3)

d0 = [2, 15, 5, 9, 7, 6, 4, 12, 5, 4, 2, 64, 5, 6, 4, 2, 3, 54, 45, 4, 44]
bucket_sort(d0)
