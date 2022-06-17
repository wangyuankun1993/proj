# -*- coding: utf-8 -*-
# Product Name: PyCharm
# Project Name: Algorithm_DataStructure
# File Name: recursion.py
# Date: 2022/06/04 11:45:34
# Author: wangyuankun
# Function: This file is to achieve recursion function.
def countdown(i):
    print(i)
    if i <= 0:
        return
    else:
        countdown(i-1)

countdown(10000)