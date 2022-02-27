# -*- coding:utf-8 -*-
# Product Name: PyCharm
# Project Name: proj
# File Name: bytesio.py
# Date: 2022/02/15 00:05:37
# Author: wangyuankun
# Function: This file is to achieve xxx function!
from io import BytesIO
f = BytesIO()
f.write('wangyuankun'.encode('utf-8'))
print(f.getvalue())
