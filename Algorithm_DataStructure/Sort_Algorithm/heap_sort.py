# -*- coding:utf-8 -*-
# Product Name: PyCharm
# Project Name: proj
# File Name: heap_sort.py
# Date: 2022/02/11 13:45:18
# Author: wangyuankun
# Function: This file is to achieve xxx function!
import numpy as np
def sort_max(data):
    for i in range(len(data) - 1):
        for j in range(len(data) - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data

def heap_min(data, type):
    index = 0
    if not type:
        for i in range(len(data[1:])):
            if data[index] > data[i + 1]:
                index = i + 1
        data[0], data[index] = data[index], data[0]
        return data
    else:
        for i in range(len(data[1:])):
            if data[index] < data[i + 1]:
                index = i + 1
        data[0], data[index] = data[index], data[0]
        return data

def heap_adj(data, type): # data original heap, type=1 is max heap, type=0 is min heap
    length = len(data)
    floor = int(np.log2(length))
    for i in range(floor, 0, -1):
        for j in range(2 ** floor - 1, 2 ** (floor - i) - 1, -1):
            d_mid = [data[j - 1]]
            if j * 2 <= length:
                d_mid.append(data[j * 2 - 1])
            if j * 2 + 1 <= length:
                d_mid.append(data[j * 2])
            d_mid = heap_min(d_mid, type)
            if len(d_mid) == 2:
                data[j - 1], data[j * 2 - 1] = d_mid[0], d_mid[1]
            elif len(d_mid) == 3:
                data[j - 1], data[j * 2 - 1], data[j * 2] = d_mid[0], d_mid[1], d_mid[2]
    return data

d0 = [2, 15, 5, 9, 7, 6, 4, 12, 5, 4, 2, 64, 5, 6, 4, 2, 3, 54, 46, 4, 44]
d1 = []
for i in range(len(d0)):
    data = heap_adj(d0, 0)
    d1.append(d0[0])
    del d0[0]

print(d1)
