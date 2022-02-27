# -*- coding:utf-8 -*-
# Product Name: PyCharm
# Project Name: proj
# File Name: server.py
# Date: 2022/02/19 22:37:19
# Author: wangyuankun
# Function: This file is to achieve xxx function!
from wsgiref.simple_server import make_server

from hello import application

httpd = make_server('', 8000, application)
print('Serving HTTP on port 8000...')

httpd.serve_forever()
