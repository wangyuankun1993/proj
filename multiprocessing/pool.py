# -*- coding:utf-8 -*-
# Product Name: PyCharm
# Project Name: proj
# File Name: pool.py
# Date: 2022/02/17 10:54:34
# Author: wangyuankun
# Function: This file is to achieve xxx function!
from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print('Run task %s (%s) ...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s run %.2f seconds.' % (name, end - start))

if __name__ == '__main__':
    print('Parend process %s.' % os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')
