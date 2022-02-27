# -*- coding:utf-8 -*-
# Product Name: PyCharm
# Project Name: proj
# File Name: fork.py
# Date: 2022/02/16 23:51:58
# Author: wangyuankun
# Function: This file is to achieve xxx function!
import os
print('Process %s start...' % os.getpid())
pid = os.fork()
if pid == 0:
    print('I am child process %s and my parent is %s.' % (os.getpid(), os.getppid()))
else:
    print('I %s just created process %s.' % (os.getpid(), pid))
