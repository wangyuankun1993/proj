# -*- coding: utf-8 -*-
# Product Name: PyCharm
# Project Name: wangyuankun
# File Name: common.py
# Date: 2021/6/17 23:45:42
# Author: wangyuankun
# Function: This file is to achieve common program !
import os, json
import core.settings
def query_user(username): # 查询用户
    filelist = os.listdir(core.settings.userinfo_dir) # 列出指定目录下的所有文件和子目录，包括隐藏文件，并以列表方式打印
    dict = {}
    for filename in filelist:
        with open(os.path.join(core.settings.userinfo_dir, filename), 'r', encoding='utf-8') as f:
            content = json.load(f) # json反序列化
            if content['username'] == username:
                dict = {'filename':filename,'content':content}
                return dict