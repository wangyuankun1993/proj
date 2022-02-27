# -*- coding:utf-8 -*-
# Product Name: PyCharm
# Project Name: proj
# File Name: requests_get.py
# Date: 2022/02/18 00:12:37
# Author: wangyuankun
# Function: This file is to achieve xxx function!
import requests
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0;Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Sari/537.36'}
url = 'https://www.douban.com/'
r = requests.get(url, headers=headers)
status = r.status_code
txt = r.text
encoding = r.encoding
print(status)
print(txt)
print(encoding)
print(r.headers)
