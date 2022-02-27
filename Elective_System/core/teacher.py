# -*- coding: utf-8 -*-
# Product Name: PyCharm
# Project Name: wangyuankun
# File Name: teacher.py
# Date: 2021/5/29 18:48:10
# Author: wangyuankun
# Function: This file is to achieve teacher interface !

from core import main

def login():
    '''
    老师登录认证
    :return: 老师对象
    '''
    name = input('输入老师姓名：')
    password = input('输入密码：')
    obj = main.Teacher.get_obj(name)
    if obj.check_password(password):
        print(f'\033[32m登陆成功\033[0m')
        return obj
    else:
        exit()

def run():
    '''
    老师操作界面
    :return:
    '''
    ojb_teacher = login()
    inp_dict = {
        '1':['开始上课','class_begin'],
        '2':['查看学员','show_students'],
        '3':['管理成绩','change_score']
    }
    while True:
        inp = main.get_cmd(inp_dict)
        if inp.lower() == 'q':
            break
        if inp in inp_dict:
            getattr(obj_teacher, inp_dict[inp][1], None)()

if __name__ == '__main__':
    run()