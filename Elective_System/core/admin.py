# -*- coding: utf-8 -*-
# Product Name: PyCharm
# Project Name: wangyuankun
# File Name: admin.py
# Date: 2021/5/26 00:03:24
# Author: wangyuankun
# Function: This file is to achieve administration !

from core import main
import hashlib

def login():
    '''
    学生登陆认证
    :return: 学生对象
    '''
    while True:
        name = input('输入管理员账号：')
        password = input('输入管理员密码：')
        password_sha1 = hashlib.sha1()
        password_sha1.update(password.encode('utf-8'))
        if name == 'admin' and password_sha1.hexdigest() == 'd033e22ae348aeb5660fc2140aec35850c4da997':
            print(f'\033[32m登陆成功\033[0m')
            break

def run():
    '''
    管理员操作界面
    :return:
    '''
    login()
    inp_dict = {
        '1':['创建学校','create_school'],
        '2':['创建班级','create_class'],
        '3':['创建老师','create_teacher'],
        '4':['创建课程','create_lesson']
    }
    while True:
        inp = main.get_cmd(inp_dict)
        if inp.lower() == 'q':
            break
        if inp in inp_dict:
            obj = getattr(main.School, inp_dict[inp][1], None)()
            obj.save()

if __name__ == '__main__':
    run()