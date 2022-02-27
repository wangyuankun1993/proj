# -*- coding:utf-8 -*-
# Product Name: PyCharm
# Project Name: proj
# File Name: reverse_iterative.py
# Date: 2022/02/02 10:54:17
# Author: wangyuankun
# Function: This file is to achieve xxx function!
def reverse_iterative(S):
    start, stop = 0, len(S)
    while start < stop - 1:
        S[start], S[stop-1] = S[stop-1], S[start]
        start, stop = start + 1, stop - 1
