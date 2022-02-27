# -*- coding:utf-8 -*-
# Product Name: PyCharm
# Project Name: proj
# File Name: sqrt.py
# Date: 2021/12/04 17:02:40
# Author: wangyuankun
# Function: This file is to achieve sqrt function!

# cmath used for complex
import cmath

num = int(input("Please input a number: "))
num_sqrt = cmath.sqrt(num)
print('{0} sqrt is {1:0.3f}+{2:0.3f}j'.format(num,num_sqrt.real,num_sqrt.imag))


