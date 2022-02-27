# -*- coding: utf-8 -*-
# Product Name: PyCharm
# Project Name: wangyuankun
# File Name: multiprocessing.py
# Date: 2021/6/23 20:24:35
# Author: wangyuankun
# Function: This file is to achieve xxx !
from multiprocessing import Process
import time

class MyProcess(Process):
    def __init__(self):
        super(MyProcess, self).__init__()

    def run(self):
        time.sleep(1)
        print('hello', self.name, time.ctime())

if __name__ == '__main__':
    p_list = []
    for i in range(3):
        p = MyProcess()
        p.start()
        p_list.append(p)

    for p in p_list:
        p.join()

    print('end')
