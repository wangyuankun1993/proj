# -*- coding: utf-8 -*-
# Product Name: PyCharm
# Project Name: guess_idiom
# File Name: config
# Date: 2022/01/16 22:45:15
# Author: wangyuankun
# Function: This file is to achieve config!
class Config:
    SECRET_KEY = 'wangyuankun1993'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:wangyuankun1993@localhost/idiom?charset=utf8mb4"

    # 小程序配置信息
    AppID = 'wx248caf7447989b19' # 小程序的AppID
    AppSecret = '47094793776c19aff0ab0c971dbf505d'