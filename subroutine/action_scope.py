# -*- coding:utf-8 -*-
# Product Name: PyCharm
# Project Name: subroutine
# File Name: action_scope
# Date: 2021/02/16 15:45:35
# Author: wangyuankun
# Function: This file is achieve xxx!
def outer():
    count = 10
    def iner():
        nonlocal count
        print(count)
        count = 5
        print(count)
    iner()
outer()