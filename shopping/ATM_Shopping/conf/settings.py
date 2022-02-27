# -*- coding:utf-8 -*-
# Product Name: PyCharm
# Project Name: shopping
# File Name: settings
# Date: 2021/03/25 23:30:40
# Author: wangyuankun
# Function: This file is to achieve environment variables information!
import time
import os
from core import users as u

# Administor account and password
adminName = 'wangyuankun'
adminPassword = 'wangyuankun1993'

# Current time
timeYear = time.strftime('%Y%m%d', time.localtime(time.time()))
timeDay = time.strftime('%H%M%S', time.localtime(time.time()))

# Credit card limit
creditLimit = 15000

# User information file
userInfoFile = '../db/user-info.json'

# Goods information file
goodsInfoFile = '../db/goods-info.json'

# Shopping cart file
def ShoppingCartFile(username,year=timeYear,day=timeDay):
    dirs = '../db/shoppingCart/%s' % username
    if not os.path.exists(dirs):
        os.makedirs(dirs)
    shoppingInfoFile = '%s/shopping-info_%s%s.json' % (dirs,year,day)
    return shoppingInfoFile

# Log file
logFile = '../log/atm.log'

# decorator
def log(func):
    def wrapper(*args,**kwargs):
        users = u.Users().getUser()
        f = open('logFile', 'a', encoding='utf-8')
        if func.__doc__ != 'check balance' and func.__doc__ != 'change password':
            f.write('%s\t%s%s%s yuan\n' % (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()),
                                           users[args[1]]['ussername'], func.__doc__, args[-1]))
        else:
            f.write('%s\t%s%s\n' % (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()),
                                           users[args[1]]['ussername'], func.__doc__))
        f.close()
        return func(*args,**kwargs)
    return wrapper

