# -*- coding:utf-8 -*-
# Product Name: PyCharm
# Project Name: proj
# File Name: unique2.py
# Date: 2022/02/01 17:24:33
# Author: wangyuankun
# Function: This file is to achieve xxx function!
def unique2(S):
    temp = sorted(S)
    for j in range(1, len(temp)):
        if temp[j-1] == temp[j]:
            return False
    return True
