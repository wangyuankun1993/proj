# -*- coding:utf-8 -*-
# Product Name: PyCharm
# Project Name: subroutine
# File Name: decorator
# Date: 2021/02/18 12:29:21
# Author: wangyuankun
# Function: This file is achieve xxx!
import time_output
def show_time(f):
    def inner():
        start_time = time_output.time_output()
        f()
        time_output.sleep(2)
        end_time = time_output.time_output()
        interval = end_time - start_time
        print('Interval is %s' % interval)
    return inner
@show_time #foo = show_time(foo)
def foo():
    print('foo...')
foo()