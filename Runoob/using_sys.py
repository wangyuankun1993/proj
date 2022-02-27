# -*- coding:utf-8 -*-
# Product Name: PyCharm
# Project Name: proj
# File Name: using_sys.py
# Date: 2022/01/26 14:17:37
# Author: wangyuankun
# Function: This file is to achieve xxx function!
import sys

print('Command line as follow:')
for i in sys.argv:
    print(i)

print('\n\nPython path: ', sys.path, '\n')
