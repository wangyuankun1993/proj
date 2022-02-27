# -*- coding:utf-8 -*-
# Product Name: PyCharm
# Project Name: proj
# File Name: half_insertion_sort.py
# Date: 2022/02/10 13:45:05
# Author: wangyuankun
# Function: This file is to achieve xxx function!
def half_insertion_sort():
    d0 = [2, 15, 5, 9, 7, 6, 4, 12, 5, 4, 2, 64, 5, 6, 4, 2, 3, 54, 45, 4, 44]
    d1 = [d0[0]]
    del d0[0]
    for i in d0:
        index_now = [0, len(d1)]
        while True:
            index = index_now[0] + int((index_now[1] - index_now[0]) / 2)
            if i == d1[index]:
                d1.insert(index+1, i)
                break
            elif index in index_now:
                d1.insert(index+1, i)
                break
            elif i > d1[index]:
                index_now[0] = index
            elif i < d1[index]:
                index_now[1] = index
    return d1

a = half_insertion_sort()
print(a)
