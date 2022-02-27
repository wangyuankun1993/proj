# -*- coding:utf-8 -*-
# Product Name: PyCharm
# Project Name: proj
# File Name: arguments.py
# Date: 2022/01/26 00:14:52
# Author: wangyuankun
# Function: This file is to achieve xxx function!
def printinfo(arg1, *vartuple, **vardict):
    "print every argument"
    print(arg1)
    print(vartuple)
    print(vardict)

printinfo(50,60,70,name='wangyuankun',age=30)
