# -*- coding:utf-8 -*-
# Product Name: PyCharm
# Project Name: proj
# File Name: urllib_ex.py
# Date: 2022/02/17 23:28:55
# Author: wangyuankun
# Function: This file is to achieve xxx function!
from urllib import request

with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
	data = f.read()
	print('Status:', f.status, f.reason)
	for k, v in f.getheaders():
		print('%s: %s' % (k, v))
	print('Data:', data.decode('utf-8'))
