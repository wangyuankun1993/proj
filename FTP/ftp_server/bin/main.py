# -*- coding: utf-8 -*-
# Product Name: PyCharm
# Project Name: wangyuankun
# File Name: main.py
# Date: 2021/6/17 21:36:35
# Author: wangyuankun
# Function: This file is to achieve server program !
import os, sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # 获取当前文件的上两级目录
sys.path.append(BASE_DIR)

import socketserver
from core.server import MyTCPHandler
from core.usermanagement import UserOpr

if __name__ == '__main__':
    mainpage = '''
    主页
        1.启动服务器
        2.进入用户管理
        退出请按q
    '''

    while True:
        print('\033[1;35m{}\033[0m'.format(mainpage))
        choice = input('>>>:')
        if choice == 'q':
            exit()
        elif choice == '1':
            HOST, PORT = 'localhost', 9999
            server = socketserver.ThreadingTCPServer((HOST, PORT), MyTCPHandler)
            server.serve_forever()
        elif choice == '2':
            useropr = UserOpr()
            # useropr.query_all_user() # 查询所有用户信息
            useropr.interactive()
        else:
            print('\033[1;31m输入错误，请重新输入\033[0m')
            continue