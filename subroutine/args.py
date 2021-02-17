# -*- coding:utf-8 -*-
# Product Name: PyCharm
# Project Name: subroutine
# File Name: args
# Date: 2021/02/15 19:26:26
# Author: wangyuankun
# Function: This file is achieve xxx!
de args_info(*args, **kwargs):
    print(args)
    print(kwargs)
    for i in kwargs:
        print("%s: %s" % (i, kwargs[i]))
args_info('wangyuankun', '26', love='liuchunyu', age='28')
# The args is on the left, the kwargs is on the right.
# The default args is on the first.