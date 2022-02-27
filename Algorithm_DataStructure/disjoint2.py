# -*- coding:utf-8 -*-
# Product Name: PyCharm
# Project Name: proj
# File Name: disjoint2.py
# Date: 2022/02/01 17:15:56
# Author: wangyuankun
# Function: This file is to achieve xxx function!
def disjoint2(A, B, C):
    for a in A:
        for b in B:
            if a == b:
                for c in C:
                    return False
    return True
