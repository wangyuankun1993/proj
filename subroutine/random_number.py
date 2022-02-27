# -*- coding:utf-8 -*-
# Product Name: PyCharm
# Project Name: subroutine
# File Name: random
# Date: 2021/02/26 23:40:25
# Author: wangyuankun
# Function: This file is achieve xxx!
import random

def verify_code():
    code = ''
    for i in range(5):
        code_number = random.randrange(10)
        code += str(code_number)
    print(code)

verify_code()