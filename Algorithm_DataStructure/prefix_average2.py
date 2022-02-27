# -*- coding:utf-8 -*-
# Product Name: PyCharm
# Project Name: proj
# File Name: prefix_average2.py
# Date: 2022/02/01 16:49:57
# Author: wangyuankun
# Function: This file is to achieve xxx function!
def prefix_average2(S):
    n = len(S)
    A = [0] * n
    for j in range(n):
        A[j] = sum(S[0:j+1]) / (j + 1)
    return A
