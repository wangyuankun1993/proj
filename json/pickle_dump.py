# -*- coding:utf-8 -*-
# Product Name: PyCharm
# Project Name: json
# File Name: pickle_dump
# Date: 2021/03/20 17:44:59
# Author: wangyuankun
# Function: This file is achieve xxx!
import pickle

def foo():
    print("hello world!")

data = pickle.dumps(foo)
f = open('Pickle_log', 'wb')
f.close()