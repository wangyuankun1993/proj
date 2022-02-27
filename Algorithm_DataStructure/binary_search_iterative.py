# -*- coding:utf-8 -*-
# Product Name: PyCharm
# Project Name: proj
# File Name: binary_search_iterative.py
# Date: 2022/02/02 10:44:29
# Author: wangyuankun
# Function: This file is to achieve xxx function!
def binary_search_iterative(data, target):
    low = 0
    high = len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False
