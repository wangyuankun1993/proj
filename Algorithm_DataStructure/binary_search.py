# -*- coding:utf-8 -*-
# Product Name: PyCharm
# Project Name: proj
# File Name: binary_search.py
# Date: 2022/02/01 20:24:42
# Author: wangyuankun
# Function: This file is to achieve xxx function!
def binary_search(data, target, low, high):
    """
    Return True if target is found in indicated portion of a Python list.
    The search only considers the portion from data[low] to data[high] inclusive.
    """
    if low > high:
        return False # interval is empty, no match
    else:
        mid = (high + low) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binary_search(data, target, low, mid - 1)
        else:
            return binary_search(data, target, mid + 1, high)

a = binary_search([1,3,4,5,7,8,10], 8, 0, 6)
print(a)
