# -*- coding:utf-8 -*-
# Product Name: PyCharm
# Project Name: proj
# File Name: quadratic_equation.py
# Date: 2021/12/04 17:12:10
# Author: wangyuankun
# Function: This file is to achieve quadratic equation function!

# ax**2 + bx +c = 0
# a != 0

import cmath

a = float(input('Please input a: '))
b = float(input('Please input b: '))
c = float(input('Please input c: '))

d = (b**2) - (4*a*c)

sol1 = (-b+cmath.sqrt(d))/(2*a)
sol2 = (-b-cmath.sqrt(d))/(2*a)

print('The result are {0} and {1}.'.format(sol1,sol2))

