# -*- coding:utf-8 -*-
# Product Name: PyCharm
# Project Name: proj
# File Name: Fibonacci.py
# Date: 2021/12/01 20:56:31
# Author: wangyuankun
# Function: This file is to achieve Fibonacci function!
import sys

def fibonacci(n): # generator function
    a, b, counter = 0, 1, 0
    while True:
        if counter > n:
            return
        yield a
        a, b = b, a + b
        counter += 1
f = fibonacci(10) # f is a iterator, return from generator
