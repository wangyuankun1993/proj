# -*- coding:utf-8 -*-
# Product Name: PyCharm
# Project Name: proj
# File Name: disjoint1.py
# Date: 2022/02/01 17:11:55
# Author: wangyuankun
# Function: This file is to achieve xxx function!
def disjoint1(A, B, C):
    for a in A:
        for b in B:
            for c in C:
                if a == b == c:
                    return False
    return True
