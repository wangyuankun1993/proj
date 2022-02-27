# -*- coding:utf-8 -*-
# Product Name: PyCharm
# Project Name: shopping
# File Name: main
# Date: 2021/04/05 22:39:54
# Author: wangyuankun
# Function: This file is to achieve total function!
import os, sys
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)
from core import goods as g
from core import atm as a
from conf import settings as ss
from core import users as u
from core import shopping as s

def checkAdmin():
    '''check admin account and password'''
    i = 2
    while i >= 0:
        username = input('Please input admin account: ')
        if username == ss.adminName:
            j = 2
            while j >= 0:
                password = input('Please input admin password: ')
                if password == ss.adminPassword:
                    return True
                else:
                    print('Admin password incorrect!')
                    if j == 0:
                        print('Account has been locked, please try again after ten minutes!')
                        return False
                    else:
                        print('You will have %s times to try!' % j)
                j -= 1
        else:
            print('Admin account incorrect!')
            if i != 0:
                print('You will have %s times to try!' % i)
            else:
                print('Account has been locked, please try again after ten minutes!')
        i -= 1
    return False

def averageUser():
    # usual user action
    print('''
    Please select action:
    1. Shopping
    2. ATM action
    ''')
    while True:
        choice = input().strip()
        if choice == '1':
            s.run()
            break
        elif choice == '2':
            a.run()
            break
        else:
            print('Invalid input!')

def adminManagement():
    '''admin action'''
    print('''
    Please select action:
    1. Goods management
    2. Users management
    ''')
    while True:
        choice = input().strip()
        if choice == '1':
            g.run()
            break
        elif choice == '2':
            u.run()
            break
        else:
            print('Invalid input!')

def run():
    '''program entrance foo'''
    print('''
    Welcome to ATM & Shopping function!
    Please select action:
    1. Usual user
    2. Admin
    ''')
    while True:
        choice = input().strip()
        if choice == '1':
            averageUser()
            break
        elif choice == '2':
            if checkAdmin():
                adminManagement()
            break
        else:
            print('Invalid input!')

if __name__ == '__main__':
    run()