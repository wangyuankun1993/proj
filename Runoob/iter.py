# -*- coding:utf-8 -*-
# Product Name: PyCharm
# Project Name: proj
# File Name: iter.py
# Date: 2022/01/25 22:26:59
# Author: wangyuankun
# Function: This file is to achieve xxx function!
class MyNumbers():
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)
