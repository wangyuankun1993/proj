# -*- coding:utf-8 -*-
# Product Name: PyCharm
# Project Name: proj
# File Name: multiprocess1.py
# Date: 2022/02/17 10:48:05
# Author: wangyuankun
# Function: This file is to achieve xxx function!
from multiprocessing import Process
import os

def run_proc(name):
    print('Run child process %s (%s) ...' % (name, os.getpid()))

if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')
