# -*- coding: utf-8 -*-
# Product Name: PyCharm
# Project Name: wangyuankun
# File Name: student.py
# Date: 2021/5/29 00:06:51
# Author: wangyuankun
# Function: This file is to achieve student interface !

from core import main

def login():
    '''
    学生认证登录
    :return: 学生对象
    '''

    name = input('输入学生姓名：')
    password = input('输入密码：')
    obj = main.Student.get_obj(name)
    if obj.check_password(password):
        print(f'\033[32m登陆成功\033[0m')
        return obj
    else:
        exit()

def register():
    '''
    学生注册
    :return:
    '''
    obj_stu = main.Student.create_student()
    obj_stu.save()
    return False

def run():
    '''
    学生操作界面
    :return:
    '''
    inp_1 = {
        '1':['注册',register],
        '2':['登陆',login]
    }
    while True:
        obj_student = False
        inp = main.get_cmd(inp_1)
        if inp in inp_1:
            obj_student = inp_1[inp][1]()
        if obj_student:
            break

    inp_2 = {
        '1':['报名课程','buy_lesson'],
        '2':['查看成绩','show_score']
    }
    while True:
        inp = main.get_cmd(inp_2)
        if inp.lower() == 'q':
            break
        if inp in inp_2:
            getattr(obj_student, inp_2[inp][1],None)()

if __name__ == '__main__':
    run()