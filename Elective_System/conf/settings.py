# -*- coding: utf-8 -*-
# Product Name: PyCharm
# Project Name: wangyuankun
# File Name: settings.py
# Date: 2021/5/25 23:55:06
# Author: wangyuankun
# Function: This file is to achieve local database route !

import os

# 设置本地数据库路径
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = {
    'school':f'{path}/db/school',
    'class':f'{path}/db/class',
    'teacher':f'{path}/db/teacher',
    'student':f'{path}/db/student',
    'lesson':f'{path}/db/lesson'
}