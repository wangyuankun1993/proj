# -*- coding: utf-8 -*-
# Product Name: PyCharm
# Project Name: wangyuankun
# File Name: settings.py
# Date: 2021/6/17 22:57:10
# Author: wangyuankun
# Function: This file is to achieve configuration !
import os, configparser, logging

# 读取配置文件 #
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # 获取当前文件的上两级目录
config_file = os.path.join(base_dir, 'conf/server.conf') # 将2个路径组合后返回
cf = configparser.ConfigParser()
cf.read(config_file, encoding='utf-8')

# 设定日志目录 #
'''先判断日志文件是否存在，如果不存，则创建'''
if os.path.exists(cf.get('log', 'usermgr_log')):
    usermgr_log = cf.get('log', 'usermgr_log')
else:
    usermgr_log = os.path.join(base_dir, 'log/usermgr.log')

# 设定用户上传文件目录，这边用于创建用户家目录使用 #
if os.path.exists(cf.get('upload', 'upload_dir')):
    file_dir = cf.get('upload', 'upload_dir')
else:
    file_dir = os.path.join(base_dir, 'user_files')

# 设定用户信息存储位置 #
if os.path.exists(cf.get('userinfo', 'userinfo_dir')):
    userinfo_dir = cf.get('userinfo', 'userinfo_dir')
else:
    userinfo_dir = os.path.join(base_dir, 'user_info')

# 设置日志格式 #
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s % (levelname)s % (message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename=usermgr_log,
                    filemode='a+')