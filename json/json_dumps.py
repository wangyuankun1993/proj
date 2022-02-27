# -*- coding:utf-8 -*-
# Product Name: PyCharm
# Project Name: json
# File Name: json_test
# Date: 2021/03/20 17:17:46
# Author: wangyuankun
# Function: This file is achieve xxx!
import json

dict = {'name':'wangyuankun', 'age':'25', 'height':165}
data = json.dumps(dict)
f = open('json_log', 'w')
f.write(data)
f.close()