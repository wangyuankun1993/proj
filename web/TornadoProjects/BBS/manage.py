# -*- coding: utf-8 -*-
# Product Name: PyCharm
# Project Name: BBS
# File Name: manage
# Date: 2022/01/15 12:41:43
# Author: wangyuankun
# Function: This file is to achieve management!
import os
import sys
import socket
from tornado import web, ioloop, httpserver, process, netutil
from router import ROUTERS
from conf import SETTINGS, DATABASE
from utils.logger import logger

log = logger('admin')

class Application(web.Application): # 应用类
    def __init__(self):
        super(Application, self).__init__(ROUTERS, **SETTINGS)

if __name__ == '__main__':
    args = sys.argv[1:]
    if args[0] == 'run': # 运行项目
        app = Application()
        print("Starting server on port 9999...")
        server = httpserver.HTTPServer(app)
        server.listen(9999) # 端口
        ioloop.IOLoop.instance().start() # 启动实例
    elif args[0] == 'dbshell': # 连接数据库
        config = DATABASE.get('default', {})
        os.system(f'mysql -u {user} -p {password} -D {database} -A'.format(
            user = config.get('user', 'root'),
            password = config.get('password', ''),
            database = config.get('database', 'bbs')
        ))
    elif args[0] == 'migrate': # 迁移
        config = DATABASE.get('default', {})
        init_sql = 'mysql -u {user} -p {password} -D {database} -A < database/migration.sql'.format(
            user = config.get('user', 'root'),
            password = config.get('password', ''),
            database = config.get('database', 'bbs')
        )
        print('Initializing tables to database {}...'.format(config.get('database')))
        data = os.system(init_sql)
        if data == 256:
            log.info('Seems like you haven\'t create the database, try:\n \'create database bbs default character set utf8;\'')
            print('Seems like you haven\'t create the database, try:\n \'create database bbs default character set utf8;\'')
        print('Completed.')
    elif args[0] == 'shell': # 打开ipython
        a = os.system('pip list | grep -w "ipython" 1>/dev/null')
        if a:
            print('Installing ipython...')
            os.system('pip install ipython')
        os.system('ipython')
    elif args[0] == 'help': # 帮助
        print("""
        following arguments available:
        <migrate> for migrating tables to your database,
        <shell> for using ipython shell,
        <dbshell> connect current database,
        <run> run a tornado web server.
        """)
    else:
        print('Arguments Error. Using \'help\' get help.')