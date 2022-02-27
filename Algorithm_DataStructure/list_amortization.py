# -*- coding:utf-8 -*-
# Product Name: PyCharm
# Project Name: proj
# File Name: list_amortization.py
# Date: 2022/02/02 16:18:16
# Author: wangyuankun
# Function: This file is to achieve xxx function!
from time import time
def compute_average(n):
    data = []
    start = time()
    for k in range(n):
        data.append(None)
    end = time()
    return (end - start) / n

print(compute_average(100000))
