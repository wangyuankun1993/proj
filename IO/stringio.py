# -*- coding:utf-8 -*-
# Product Name: PyCharm
# Project Name: proj
# File Name: stringio.py
# Date: 2022/02/15 00:01:53
# Author: wangyuankun
# Function: This file is to achieve xxx function!
from io import StringIO
f = StringIO()
f.write('hello')
f.write(' ')
f.write('world')
print(f.getvalue())
