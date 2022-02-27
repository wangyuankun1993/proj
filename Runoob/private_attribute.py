# -*- coding:utf-8 -*-
# Product Name: PyCharm
# Project Name: proj
# File Name: private_variable.py
# Date: 2022/01/27 14:23:06
# Author: wangyuankun
# Function: This file is to achieve xxx function!
class JustCounter():
    __secretCount = 0 # private variable
    publicCount = 0 # public variable

    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print(self.__secretCount)

counter = JustCounter()
counter.count()
counter.count()

print(counter.publicCount)
print(counter.__secretCount)
