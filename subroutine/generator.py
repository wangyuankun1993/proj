# -*- coding:utf-8 -*-
# Product Name: PyCharm
# Project Name: subroutine
# File Name: generator
# Date: 2021/02/28 15:02:11
# Author: wangyuankun
# Function: This file is achieve xxx!
def fib(times):
    a, b, n = 1, 1, 0
    while n <= times:
        yield a
        a, b = b, a+b
        n += 1

result = fib(5)
print(result)