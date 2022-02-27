# -*- coding:utf-8 -*-
# Product Name: PyCharm
# Project Name: json
# File Name: shelve
# Date: 2021/03/20 18:16:32
# Author: wangyuankun
# Function: This file is achieve xxx!
import shelve

shelve_file = shelve.open('data')
languages = ['C', 'C++', 'Java', 'Python']
shelve_file['languages'] = languages
shelve_file.close()