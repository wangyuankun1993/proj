# -*- coding:utf-8 -*-
# Product Name: PyCharm
# Project Name: proj
# File Name: prefix_average1.py
# Date: 2022/02/01 16:18:26
# Author: wangyuankun
# Function: This file is to achieve xxx function!
def prefix_average1(S):
    n = len(S)
    A = [0] * n
    for j in range(n):
        total = 0
        for i in range(j+1):
            total += S[i]
        A[j] = tatal / (j+1)
    return A
