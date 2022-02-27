# -*- coding:utf-8 -*-
# Product Name: PyCharm
# Project Name: proj
# File Name: quick_sort.py
# Date: 2022/02/11 13:18:46
# Author: wangyuankun
# Function: This file is to achieve xxx function!
def quick_sort(data):
    d = [[], [], []]
    d_pivot = data[-1]
    for i in data:
        if i < d_pivot:
            d[0].append(i)
        elif i > d_pivot:
            d[2].append(i)
        else:
            d[1].append(i)

    if len(d[0]) > 1:
        d[0] = quick_sort(d[0])
    if len(d[2]) > 1:
        d[2] = quick_sort(d[2])

    d[0].extend(d[1])
    d[0].extend(d[2])
    return d[0]

if __name__ == '__main__':
    d0 = [2, 15, 5, 9, 7, 6, 4, 12, 5, 4, 2, 64, 5, 6, 4, 2, 3, 54, 45, 4, 44]
    d1 = quick_sort(d0)
    print(d1)
