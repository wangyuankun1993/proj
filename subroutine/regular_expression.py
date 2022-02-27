# -*- coding:utf-8 -*-
# Product Name: PyCharm
# Project Name: subroutine
# File Name: regular_expression
# Date: 2021/03/06 22:56:25
# Author: wangyuankun
# Function: This file is achieve xxx!
import re

ret = re.findall('w\w{2}l', 'hello world')
print(ret)
ret = re.findall('w..l', 'hello world') #. represent one character
print(ret)
ret = re.findall('^hello', 'hello world')
print(ret)
ret = re.findall('kun$', 'wangyuankun')
print(ret)
ret = re.findall('w.*n', 'wangyuankun')
print(ret)
ret = re.findall('a+b', 'aaab')
print(ret)
ret = re.findall('a?b', 'aaab')
print(ret)
ret = re.findall('a{5}b', 'aaaaab')
print(ret)
ret = re.findall('a*b', 'aaaab') # *={0,+oo}  +={1,+oo}  ?={0,1}
print(ret)
ret = re.findall('[0-9a-zA-Z]', 'ab2cdef3gx5*')
print(ret)
ret = re.findall('[0-9,a-z,A-Z]', 'ab2cdef3gx5*')
print(ret)
ret = re.findall('\d{3}', '123456')
print(ret)
ret = re.findall('\syuan', 'wang yuan kun')
print(ret)

ret = re.search('wang', 'wangyuankun').group()
print(ret)

ret = re.findall(r'\\', 'wang\yuankun')
print(ret)

ret = re.match('wang', 'wangyuankun')
print(ret.group())

ret = re.split('[a,u]', 'wangyuankun')
print(ret)

ret = re.sub('yuan', 'chun', 'wangyuankun')
print(ret)

ret = re.findall('(?P<name>\w{4})(?P<age>\d{2})', 'wang28')
print(ret)