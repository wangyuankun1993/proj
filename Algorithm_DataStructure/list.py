# -*- coding:utf-8 -*-
# Product Name: PyCharm
# Project Name: proj
# File Name: list.py
# Date: 2022/02/02 14:20:11
# Author: wangyuankun
# Function: This file is to achieve xxx function!
import sys
data = []
for i in range(30):
    a = len(data)
    b = sys.getsizeof(data)
    print('Length: {0:3d}; Size in bytes: {1:4d}'.format(a, b))
    data.append(None)
