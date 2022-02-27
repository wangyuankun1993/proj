# -*- coding:utf-8 -*-
# Product Name: PyCharm
# Project Name: proj
# File Name: queue.py
# Date: 2022/02/17 11:40:39
# Author: wangyuankun
# Function: This file is to achieve xxx function!
from multiprocessing import Process, Queue
import os, time, random

# write data process
def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())

# read data process
def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)

if __name__ == '__main__':
    q = Queue() # parent process
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start() # start subprocess pw
    pr.start() # start subprocess pr
    pw.join() # wait for end
    pr.terminate() # pr process is loop, can't wait for end and force stop
