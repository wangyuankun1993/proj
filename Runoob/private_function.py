# -*- coding:utf-8 -*-
# Product Name: PyCharm
# Project Name: proj
# File Name: private_function.py
# Date: 2022/01/27 14:41:16
# Author: wangyuankun
# Function: This file is to achieve xxx function!
class Site():
    def __init__(self, name, url):
        self.name = name # public
        self.__url = url # private
        print(self)

    def who(self):
        print("name: ", self.name)
        print("url: ", self.__url)
        print(self)

    def __foo(self): # private function
        print("This is private function!")
        print(self)

    def foo(self): # public function
        print("This is public function")
        print(self)
        self.__foo()
        print(self.__foo())

x = Site('Runoob', 'www.runoob.com')
x.who()
x.foo()
x.__foo()
