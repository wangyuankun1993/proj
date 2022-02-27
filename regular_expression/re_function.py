# -*- coding:utf-8 -*-
# Product Name: PyCharm
# Project Name: proj
# File Name: re_function.py
# Date: 2022/01/27 23:52:50
# Author: wangyuankun
# Function: This file is to achieve xxx function!
import re

print(re.match('www', 'www.runoob.com').span())
print(re.match('com', 'www.runoob.com'))

print(re.search('www', 'www.runoob.com').span())
print(re.search('com', 'www.runoob.com').span())

phone = "2004-959-559 # This is a phone number"
# delete comment
num = re.sub(r'#.*$', '', phone)
print("Phone number: ", num)
# delete non-number
num = re.sub(r'\D', '', phone)
print("Phone number: ", num)

pattern1 = re.compile(r'\d+') # match at least one number
m1 = pattern1.match('one12twothree34four')
print(m1)
m1 = pattern1.match('one12twothree34four', 2, 10)
print(m1)
m1 = pattern1.match('one12twothree34four', 3, 10)
print(m1)
print(m1.group(0))
print(m1.start(0))
print(m1.end(0))
print(m1.span())

pattern2 = re.compile(r'([a-z]+) ([a-z]+) ([a-z]+) ([a-z]+)', re.I) # re.I means without mind upper or lower case
m2 = pattern2.match('Hello World Wide Web')
print(m2)
print(m2.span(0))
print(m2.span(1))
print(m2.span(2))
print(m2.span(3))
print(m2.span(4))
print(m2.group(0))
print(m2.group(1))
print(m2.group(2))
print(m2.group(3))
print(m2.group(4))
print(m2.groups())

result1 = re.findall(r'\d+', 'runoob 123 google 456')
print(result1)
pattern3 = re.compile(r'\d+')
result2 = pattern3.findall('runoob 123 google 456')
print(result2)
result3 = pattern3.findall('run88oob123google456', 0, 10)
print(result3)

result4 = re.findall(r'(\w+)=(\d+)', 'set width=30 and height=10')
print(result4)

it = re.finditer(r'\d+', '12a32bc43jf3')
for match in it:
    print(match.group())
