# -*- coding:utf-8 -*-
# Product Name: PyCharm
# Project Name: proj
# File Name: disk_usage.py
# Date: 2022/02/01 22:33:45
# Author: wangyuankun
# Function: This file is to achieve xxx function!
import os

def disk_usage(path):
    """Return the number of bytes used by a file/folder and any descendents."""
    total = os.path.getsize(path) # account for direct usage
    if os.path.isdir(path): # if this is a directory
        for filename in os.listdir(path): # then for each child
            childpath = os.path.join(path, filename) # compose full path to child
            total += disk_usage(childpath) # add child's usage to tatal

    print('{0:<7}'.format(total), path) # descriptive output
    return total

disk_usage('/home/wangyuankun/proj/CSS')
