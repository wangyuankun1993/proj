# -*- coding:utf-8 -*-
# Product Name: PyCharm
# Project Name: proj
# File Name: hello.py
# Date: 2022/02/19 22:35:24
# Author: wangyuankun
# Function: This file is to achieve xxx function!
def application(environ, start_response):
	start_response('200 OK', [('Content-Type', 'text/html')])
	body = '<h1>Hello, %s!</h1>' % (environ['PAHT_INFO'][1:] or 'web')
	return [body.encode('utf-8')]
