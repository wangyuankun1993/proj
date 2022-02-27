# -*- coding:utf-8 -*-
# Product Name: PyCharm
# Project Name: subroutine
# File Name: function
# Date: 2021/02/15 17:42:53
# Author: wangyuankun
# Function: This file is achieve xxx!
def adder(*args):
    print(args)
    sum = 0
    for i in args:
        sum += i
    print(sum)
adder(1, 2, 3, 4, 5)
