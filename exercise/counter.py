# -*- coding:utf-8 -*-
# Product Name: PyCharm
# Project Name: proj
# File Name: counter.py
# Date: 2022/02/17 21:33:43
# Author: wangyuankun
# Function: This file is to achieve xxx function!
from collections import Counter

c = Counter()
for ch in 'Programming':
	c[ch] = c[ch] + 1

print(c)
