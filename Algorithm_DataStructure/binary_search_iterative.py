# -*- coding:utf-8 -*-
# Product Name: PyCharm
# Project Name: proj
# File Name: binary_search_iterative.py
# Date: 2022/02/02 10:44:29
# Author: wangyuankun
# Function: This file is to achieve xxx function!
def binary_search_iterative(list, target):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) // 2
        if list[mid] == target:
            return mid
        elif list[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return None

obj = binary_search_iterative([1, 3, 5, 7, 9], -1)
print(obj)