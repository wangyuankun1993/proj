# -*- coding:utf-8 -*-
# Product Name: PyCharm
# Project Name: multiprocessing
# File Name: yield.py
# Date: 2021/06/23 21:24:13
# Author: wangyuankun
# Function: This file is to achieve xxx function!
import time
import queue

def consumer(name):
    print('--->starting eating baozi...')
    while True:
        new_baozi = yield
        print('[%s] is eating baozi %s' % (name, new_baozi))

def producer():
    r = con.__next__()
    r = con2.__next__()
    n = 0
    while n < 5:
        n += 1
        print('\033[32;1m[producer]\033[0m is making baozi %s' % n)
        con.send(n)
        con2.send(n)


if __name__ == '__main__':
    con = consumer('c1')
    con2 = consumer('c2')
    p = producer()
