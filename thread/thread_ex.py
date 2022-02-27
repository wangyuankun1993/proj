# -*- coding:utf-8 -*-
# Product Name: PyCharm
# Project Name: proj
# File Name: thread_ex.py
# Date: 2022/02/17 13:02:42
# Author: wangyuankun
# Function: This file is to achieve xxx function!
import time, threading

def loop():
    print('Thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n += 1
        print('Thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('Thread %s ended' % threading.current_thread().name)

print('Thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='wangyuankun')
t.start()
t.join()
print('Thread %s ended.' % threading.current_thread().name)
