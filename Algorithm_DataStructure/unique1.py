# -*- coding:utf-8 -*-
# Product Name: PyCharm
# Project Name: proj
# File Name: unique1.py
# Date: 2022/02/01 17:20:14
# Author: wangyuankun
# Function: This file is to achieve xxx function!
def unique1(S):
    for j in range(len(S)):
        for k in range(j+1, len(S)):
            if S[j] == S[k]:
                return False
    return True
