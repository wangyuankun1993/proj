# -*- coding:utf-8 -*-
# Product Name: PyCharm
# Project Name: json
# File Name: json_loads
# Date: 2021/03/20 17:25:15
# Author: wangyuankun
# Function: This file is achieve xxx!
import json

f = open('json_log', 'r')
data1 = f.read()
data2 = json.loads(data1)
print(data2['name'])