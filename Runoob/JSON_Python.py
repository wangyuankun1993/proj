# -*- coding:utf-8 -*-
# Product Name: PyCharm
# Project Name: proj
# File Name: JSON_Python.py
# Date: 2021/12/05 23:07:21
# Author: wangyuankun
# Function: This file is to achieve Python transform to JSON function!

import json

# Python dict transform to JSON object
data = {
    'no': 1,
    'name': 'Runoob',
    'url':'http://www.runoob.com'
}

json_str = json.dumps(data)

print("Python original data:", repr(data))
print("JSON object:", json_str)

# JSON object transform to Python dict
data2 = json.loads(json_str)
print("data2['name']:", data2['name'])
print("data2['url']:", data2['url'])
