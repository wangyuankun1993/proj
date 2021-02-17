# -*- coding:utf-8 -*-
# Product Name: PyCharm
# Project Name: subroutine
# File Name: fibonacci
# Date: 2021/02/17 13:19:27
# Author: wangyuankun
# Function: This file is achieve xxx!
def fibo(n):
    if n <= 1:
        return n
    return fibo(n-1) + fibo(n-2)

print(fibo(3))