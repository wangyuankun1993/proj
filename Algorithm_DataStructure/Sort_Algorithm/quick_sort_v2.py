# -*- coding: utf-8 -*-
# Product Name: PyCharm
# Project Name: Algorithm_DataStructure
# File Name: quick_sort_v2.py
# Date: 2022/06/05 00:20:05
# Author: wangyuankun
# Function: This file is to achieve quick_sort_v2 function.
def quickSort(array):
    if len(array) < 2:
        return array # 基线条件：为空或只包含一个元素的数组是“有序”的
    else:
        pivot = array[0] # 递归条件
        less = [i for i in array[1:] if i <= pivot] # 由所有小于基准值的元素组成的子数组
        greater = [i for i in array[1:] if i > pivot] # 由所有大于基准值的元素组成的子数组
        return quickSort(less) + [pivot] + quickSort(greater)

obj = quickSort([29, 14, 45, 23, 65, 30, 32, 21, 1, 4, 5])
print(obj)