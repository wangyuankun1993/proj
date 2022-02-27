# -*- coding:utf-8 -*-
# Product Name: PyCharm
# Project Name: proj
# File Name: slot.py
# Date: 2022/02/14 23:26:34
# Author: wangyuankun
# Function: This file is to achieve xxx function!
class Student(object):
    __slots__ = ('name', 'age')

s = Student()
s.name = 'wangyuankun'
s.age = 28
s.score = 30
