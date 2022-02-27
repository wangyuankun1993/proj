# -*- coding:utf-8 -*-
# Product Name: PyCharm
# Project Name: proj
# File Name: asyncio_hello.py
# Date: 2022/02/20 16:06:10
# Author: wangyuankun
# Function: This file is to achieve xxx function!
import asyncio

@asyncio.coroutine
def hello():
	print("Hello world!")
	r = yield from asyncio.sleep(5)
	print("Hello again!")

loop = asyncio.get_event_loop()
loop.run_until_complete(hello())
loop.close()
