# -*- coding: utf-8 -*-
# Product Name: PyCharm
# Project Name: Algorithm_DataStructure
# File Name: selection_sort_v2.py
# Date: 2022/06/03 20:05:16
# Author: wangyuankun
# Function: This file is to achieve selection_sort_v2 function.
# 定义找出数组中最小元素的函数
def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

# 定义选择排序
def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest_index = findSmallest(arr)
        newArr.append(arr.pop(smallest_index))
    return newArr

obj = selectionSort([5, 3, 6, 2, 10])
print(obj)