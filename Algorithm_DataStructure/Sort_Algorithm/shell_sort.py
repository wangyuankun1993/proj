# -*- coding:utf-8 -*-
# Product Name: PyCharm
# Project Name: proj
# File Name: shell_sort.py
# Date: 2022/02/10 23:40:50
# Author: wangyuankun
# Function: This file is to achieve xxx function!
def direct_insertion_sort(d):
    d1 = [d[0]]
    for i in d[1:]:
        state = 1
        for j in range(len(d1) - 1, -1, -1):
            if i >= d1[j]:
                d1.insert(j + 1, i)
                state = 0
                break
        if state:
            d1.insert(0, i)
    return d1

def shell_sort(d): # d is unsorted array, 1 is initial increment, 1 < len(d), len(d)/2
    length = int(len(d) / 2)
    num = int(len(d) / length)
    while True:
        for i in range(length):
            d_mid = []
            for j in range(num):
                d_mid.append(d[i + j * length])
            d_mid = direct_insertion_sort(d_mid)
            for j in range(num):
                d[i + j * length] = d_mid[j]
        length = int(length / 2)
        if length == 0:
            return d
            break
        num = int(len(d) / length)

if __name__ == '__main__':
    d0 = [2, 15, 5, 9, 7, 6, 4, 12, 5, 4, 2, 64, 5, 6, 4, 2, 3, 54, 45, 4, 44]
    d1 = shell_sort(d0)
    print(d1)
