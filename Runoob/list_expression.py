# -*- coding:utf-8 -*-
# Product Name: PyCharm
# Project Name: proj
# File Name: list_expression.py
# Date: 2022/01/26 12:01:27
# Author: wangyuankun
# Function: This file is to achieve xxx function!
vec1 = [2,4,6]
vec2 = [3,5,7]
a = [x + y for x in vec1 for y in vec2]
print(a)
