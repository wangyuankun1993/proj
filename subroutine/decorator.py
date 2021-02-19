# -*- coding:utf-8 -*-
# Product Name: PyCharm
# Project Name: subroutine
# File Name: decorator
# Date: 2021/02/18 12:29:21
# Author: wangyuankun
# Function: This file is achieve xxx!
import time
def show_time(f):
    def inner():
        start_time = time.time()
        f()
        time.sleep(2)
        end_time = time.time()
        interval = end_time - start_time
        print('Interval is %s' % interval)
    return inner
@show_time #foo = show_time(foo)
def foo():
    print('foo...')
foo()