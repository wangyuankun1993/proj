# -*- coding:utf-8 -*-
# Product Name: PyCharm
# Project Name: proj
# File Name: turtle_drawStar.py
# Date: 2022/02/18 22:18:21
# Author: wangyuankun
# Function: This file is to achieve xxx function!
from turtle import *

def drawStar(x, y):
	pu()
	goto(x, y)
	pd()
	seth(0)
	for i in range(5):
		fd(40)
		rt(144)

for x in range(0, 250, 50):
	drawStar(x, 0)

done()
