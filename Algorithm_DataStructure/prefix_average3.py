# -*- coding:utf-8 -*-
# Product Name: PyCharm
# Project Name: proj
# File Name: prefix_average3.py
# Date: 2022/02/01 16:55:24
# Author: wangyuankun
# Function: This file is to achieve xxx function!
def prefix_average3(S):
    n = len(S)
    A = [0] * n
    total = 0
    for j in range(n):
        total += S[j]
        A[j] = total / (j+1)
    return A
