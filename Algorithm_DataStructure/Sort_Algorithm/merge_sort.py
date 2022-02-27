# -*- coding:utf-8 -*-
# Product Name: PyCharm
# Project Name: proj
# File Name: merge_sort.py
# Date: 2022/02/11 12:11:29
# Author: wangyuankun
# Function: This file is to achieve xxx function!
def merge_sort(data):
    half_index = int(len(data) / 2)
    d0 = data[:half_index]
    d1 = data[half_index:]
    if len(d0) > 1:
        d0 = merge_sort(d0)
    if len(d1) > 1:
        d1 = merge_sort(d1)

    index = 0
    for i in range(len(d1)):
        state = 1
        for j in range(index, len(d0)):
            if d1[i] < d0[j]:
                state = 0
                index = j + 1
                d0.insert(j, d1[i])
                break
        if state == 1:
            d0.extend(d1[i:])
            break
    return d0

if __name__ == '__main__':
    d0 = [2, 15, 5, 9, 7, 6, 4, 12, 5, 4, 2, 64, 5, 6, 4, 2, 3, 54, 45, 4, 44]
    d1 = merge_sort(d0)
    print(d1)
