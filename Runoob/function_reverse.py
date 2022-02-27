# -*- coding:utf-8 -*-
# Product Name: PyCharm
# Project Name: proj
# File Name: function_reverse.py
# Date: 2021/11/30 21:06:52
# Author: wangyuankun
# Function: This file is to achieve xxx function!
def reverseWords(input):
    inputWords = input.split(" ")
    print(inputWords)

    inputWords = inputWords[-1::-1]
    output = ' '.join(inputWords)

    return output

if __name__ == "__main__":
    input = 'I like runoob'
    rw = reverseWords(input)
    print(rw)
