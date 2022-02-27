# -*- coding: utf-8 -*-
# Product Name: PyCharm
# Project Name: wangyuankun
# File Name: level_3_menu_v1.py
# Date: 2021/1/26 23:49:32
# Author: wangyuankun
# Function: This file is to achieve three levels menu!
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
back_flag = False
exit_flag = False

while not back_flag and not exit_flag:
    for key1 in regions:
        print(key1)
    province = input("Please input province:").strip()
    if province == 'b':
        back_flag = True
    if province == 'q':
        exit_flag = True
    if province in regions:
        while not back_flag and not exit_flag:
            for key2 in regions[province]:
                print(key2)
            city = input("Please input city:").strip()
            if city == 'b':
                back_flag = True
            if city == 'q':
                exit_flag = True
            if city in regions[province]:
                while not back_flag and not exit_flag:
                    for key3 in regions[province][city]:
                        print(key3)
                    next = input("Please input next:").strip()
                    print("Last level!")
                    if next == 'b':
                        back_flag = True
                    if next == 'q':
                        exit_flag = True
                else:
                    back_flag = False
        else:
            back_flag = False
else:
    back_flag = False
