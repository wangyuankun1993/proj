# -*- coding: utf-8 -*-
# Product Name: PyCharm
# Project Name: BBS
# File Name: connect
# Date: 2022/01/15 17:01:08
# Author: wangyuankun
# Function: This file is to achieve connect!
import pymysql
from conf import DATABASE
from database import tornado_mysql
from database.tornado_mysql import pools

pymysql.install_as_MySQLdb()

class Connect(object): # 异步连接数据库类
    def __init__(self):
        self.config = DATABASE.get('default', {})
        self.connection = pymysql.connections.Connection(**self.config)
        self.cursor = self.connection.cursor()
        self.dict_cursor = self.connection.cursor(cursor=pymysql.cursors.DictCursor)

    def close(self):
        self.connection.close()
        self.dict_cursor.close()
        self.cursor.close()

def connect(): # 连接默认数据库
    config = DATABASE.get('default', {})
    conn = pymysql.connections.Connection(**config)
    return conn.cursor(cursor=pymysql.cursors.DictCursor)

def async_connect(): # 异步连接
    conf = DATABASE.get('default', {})
    conf.update({
        'autocommit': True,
        'cursorclass': tornado_mysql.cursors.DictCursor
    })
    return tornado_mysql.connect(**conf)

def async_pool(): # 连接池
    conf = DATABASE.get('default', {})
    conf.update({
        'cursorclass':tornado_mysql.cursors.DictCursor
    })
    POOL = pools.Pool(conf, max_idle_connections=1, max_recycle_sec=3)
    return POOL