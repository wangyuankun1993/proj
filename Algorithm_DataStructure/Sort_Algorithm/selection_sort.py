# -*- coding:utf-8 -*-
# Product Name: PyCharm
# Project Name: proj
# File Name: selection_sort.py
# Date: 2022/02/10 10:53:12
# Author: wangyuankun
# Function: This file is to achieve xxx function!
def selection_sort(data):
    d1 = []
    while len(data):
        min = [0, data[0]]
        for i in range(len(data)):
            if min[1] > data[i]:
                min = [i, data[i]]
        del data[min[0]] # find minimum value in left part and del from original array
        d1.append(min[1]) # add in new array
    return d1

if __name__ == '__main__':
    d0 = [2, 15, 5, 9, 7, 6, 4, 12, 5, 4, 2, 64, 5, 6, 4, 2, 3, 54, 46, 4, 44]
    d1 = selection_sort(d0)
    print(d1)
