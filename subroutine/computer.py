# -*- coding:utf-8 -*-
# Product Name: PyCharm
# Project Name: subroutine
# File Name: computer
# Date: 2021/03/10 23:07:38
# Author: wangyuankun
# Function: This file is achieve xxx!
import re

def check(s):
    flag = True
    if re.findall('[a-zA-Z]', s):
        print('Invalid')
        flag = False
    return flag

def format(s):
    s = s.replace(' ', '')
    s = s.replace('++', '+')
    return s

def cal_mul_div(s):
    ret1 = re.search('\d+\.?\d* [*/] \d+\.?\d+', s).group()
    x, y = re.split('[*/]', ret1)
    ret2 = float(x)/float(y)
    str(ret2)
    s.replace(ret1, ret2)

def cal_add_sub(s):
    ret1 = re.search('\d+\.?\d* [+/-] \d+\.?\d+', s).group()
    x, y = re.split('[+/-]', ret1)
    ret2 = float(x)-float(y)
    str(ret2)
    s.replace(ret1, ret2)

if check(source):
    strs = format(source)
    while re.search('\('):
        strs = re.search('\([^()]\)', strs).group()
        strs = cal_mul_div(strs)
        strs = cal_add_sub(strs)

source = 2+3*(4+5/2+3*5)/2+1-6/3