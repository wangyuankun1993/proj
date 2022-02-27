# -*- coding:utf-8 -*-
# Product Name: PyCharm
# Project Name: json
# File Name: pickle_loads
# Date: 2021/03/20 17:58:00
# Author: wangyuankun
# Function: This file is achieve xxx!
import pickle

def foo():
    print('hello world')

f = open('pickle_log', 'rb')
data1 = f.read()
data2 = pickle.loads(data1)
data()