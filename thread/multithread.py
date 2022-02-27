# -*- coding:utf-8 -*-
# Product Name: PyCharm
# Project Name: proj
# File Name: multithread.py
# Date: 2022/02/17 13:19:27
# Author: wangyuankun
# Function: This file is to achieve xxx function!
import time, threading

balance = 0
lock = threading.Lock()

def change_it(n):
    global balance
    balance += n
    balance -= n

def run_thread(n):
    for i in range(2000000):
        # acquire lock
        lock.acquire()
        try:
            change_it(n)
        finally:
            lock.release()

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))

t1.start()
t2.start()
t1.join()
t2.join()

print(balance)
