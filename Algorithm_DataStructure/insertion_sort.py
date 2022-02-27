# -*- coding:utf-8 -*-
# Product Name: PyCharm
# Project Name: proj
# File Name: insertion_sort.py
# Date: 2022/02/03 00:24:03
# Author: wangyuankun
# Function: This file is to achieve xxx function!
def insertion_sort(A):
    """Sort list of comparable elements into nondecreasing order."""
    for k in range(1, len(A)):
        current = A[k]
        j = k
        while j > 0 and A[j-1] > current:
            A[j] = A[j-1]
            j -= 1
        A[j] = current
    return A

list = [4, 6, 32, 5, 3, 6, 7]
i = insertion_sort(list)
print(i)
