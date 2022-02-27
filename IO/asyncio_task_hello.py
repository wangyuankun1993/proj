# -*- coding:utf-8 -*-
# Product Name: PyCharm
# Project Name: proj
# File Name: asyncio_task_hello.py
# Date: 2022/02/20 16:12:48
# Author: wangyuankun
# Function: This file is to achieve xxx function!
import threading
import asyncio

@asyncio.coroutine
def hello():
	print('Hello world! (%s)' % threading.currentThread())
	yield from asyncio.sleep(3)
	print('Hello again! (%s)' % threading.currentThread())

loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
