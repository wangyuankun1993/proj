# -*- coding:utf-8 -*-
# Product Name: PyCharm
# Project Name: proj
# File Name: thread.py
# Date: 2021/12/05 17:32:35
# Author: wangyuankun
# Function: This file is to achieve threading function!

import _thread
import time

# Define a function to thread
def print_time(threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print("%s:%s" % (threadName, time.ctime(time.time())))

# Create two threads
try:
    _thread.start_new_thread(print_time, ("Thread-1",2,))
    _thread.start_new_thread(print_time, ("Thread-2",4,))
except:
    print("Error: Can't start thread!")

while True:
    pass
