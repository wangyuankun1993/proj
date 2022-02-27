# -*- coding:utf-8 -*-
# Product Name: PyCharm
# Project Name: multiprocessing
# File Name: gevent.py
# Date: 2021/06/23 22:44:52
# Author: wangyuankun
# Function: This file is to achieve xxx function!
from greenlet import greenlet

def test1():
    print(12)
    gr2.switch()
    print(34)
    gr2.switch()

def test2():
    print(56)
    gr1.switch()
    print(78)
