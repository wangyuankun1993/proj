# -*- coding:utf-8 -*-
# Product Name: PyCharm
# Project Name: proj
# File Name: direct_insertion_sort.py
# Date: 2022/02/10 13:28:37
# Author: wangyuankun
# Function: This file is to achieve xxx function!
def direct_insertion_sort(d):
    d1 = [d[0]]
    for i in d[1:]:
        state = 1
        for j in range(len(d1) - 1, -1, -1):
            if i >= d1[j]:
                d1.insert(j + 1, i) # insert element into array
                state  = 0
                break
        if state:
            d1.insert(0, i)
    return d1

if __name__ == '__main__':
    d0 = [2, 15, 5, 9, 7, 6, 4, 12, 5, 4, 2, 64, 5, 6, 4, 2, 3, 54, 45, 4, 44]
    d1 = direct_insertion_sort(d0)
    print(d1)
