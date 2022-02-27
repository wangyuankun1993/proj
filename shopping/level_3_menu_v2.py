# -*- coding: utf-8 -*-
# Product Name: PyCharm
# Project Name: wangyuankun
# File Name: level_3_menu_v2.py
# Date: 2021/1/30 11:57:18
# Author: wangyuankun
# Function: This file is to achieve three level menu in simple way!
regions = {
    'Beijing':{
        'Chaoyang':{'Sanlitun':'Youyiku',
                    'Guomao':'NXP',
                    'Dongdan':'Wangfujing'},
        'Haidian':{'Wudaokou':'Tsinghua',
                   'Zhichunlu':'Zhizhendasha',
                   'Haidianhuangzhuang':'shibaojie'},
        'Xicheng':{'Xidan':'Zhongnanhai',
                   'Nanluoguxiang':'houhai'}
    },
    'Shanghai':{
        'Pudong':'Lujiazui',
        'Huangpu':'Waitan'
    }
}

current_layer = regions
parent_layers = []
while True:
    for key in current_layer:
        print(key)
    choice = input(">>:").strip()
    if choice in current_layer:
        parent_layers.append(current_layer)
        current_layer = current_layer[choice]
    elif choice == 'b':
        if parent_layers:
            current_layer = parent_layers.pop()
    else:
        print("Invalid input!")
