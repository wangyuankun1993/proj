# -*- coding:utf-8 -*-
# Product Name: PyCharm
# Project Name: wangyuankun
# File Name: deep_shallow_copy
# Date: 2021/02/14 17:41:07
# Author: wangyuankun
# Function: This file is achieve xxx!
import copy
name = ['wangyuankun', 'liuchunyu', 'Danny', 'Jane', [1, 2]]
name1 = name.copy()
name2 = copy.deepcopy(name)
name1[4][0] = 5
name2 [4][0] = 4
print(name)
print(name1)
print(name2)
