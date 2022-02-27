# -*- coding:utf-8 -*-
# Product Name: PyCharm
# Project Name: proj
# File Name: requests_post.py
# Date: 2022/02/18 14:35:40
# Author: wangyuankun
# Function: This file is to achieve xxx function!
import requests

url = 'https://accounts.douban.com/login'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0;Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Sari/537.36'}
r = requests.post(url, headers=headers, data={'form_eamil':'wangyuankun@aliyun.com','form_password':'wangyuankun1993'})
print(r)
