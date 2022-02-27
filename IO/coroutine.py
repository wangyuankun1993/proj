# -*- coding:utf-8 -*-
# Product Name: PyCharm
# Project Name: proj
# File Name: coroutine.py
# Date: 2022/02/20 15:48:22
# Author: wangyuankun
# Function: This file is to achieve xxx function!

def consumer():
	r = ''
	while True:
		n = yield r
		if not n:
			return
		print('[CONSUMER] Consuming %s...' % n)
		r = '200 OK'

def produce(c):
	c.send(None)
	n = 0
	while n < 5:
		n = n + 1
		print('[PRODUCER] Producing %s...' % n)
		r = c.send(n)
		print('[PRODUCER] Consumer return: %s' % r)
	c.close()
c = consumer()
produce(c)
