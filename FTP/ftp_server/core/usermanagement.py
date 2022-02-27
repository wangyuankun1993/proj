# -*- coding: utf-8 -*-
# Product Name: PyCharm
# Project Name: wangyuankun
# File Name: usermanagement.py
# Date: 2021/6/21 00:03:41
# Author: wangyuankun
# Function: This file is to achieve user management program !
import os, time, json, shutil, hashlib
import core.common

def hashmd5(self, *args):
    m = hashlib.md5()
    m.update(str(*args).encode())
    ciphertexts = m.hexdigest()
    return ciphertexts

# 用户操作类
class UserOpr(object):
    def __init__(self):
        pass

    def query_userinfo(self, username):
        query_result = core.common.query_user(username)
        if query_result != None: # 用户存在
            print(query_result)
        else:
            print('用户不存在')

    def save_userinfo(self, username): # 保存用户信息
        query_result = core.common.query_user(username) # 检查是否已存在同名用户，如果没有查询结果应该为None
        if query_result == None: # 用户不存在
            id = time.strftime('%Y%m%d%H%M%S', time.localtime()) # 将结构化时间转换成格式化的字符串
            password = '123456'
            userinfo = {
                'username':username,
                'id':id,
                'phonenumber':'',
                'password':hashmd5(password),
                'spacesize':104857600, # 初始分配100MB存储空间
                'level':1 # 会员等级，初始为1，普通会员
            }
            with open(os.path.join(core.settings.userinfo_dir, id), 'w', encoding='utf-8') as f:
                json.dump(userinfo, f)
                print('用户信息保存完毕')
                try: # 创建用户家目录
                    os.mkdir(os.path.join(core.settings.file_dir, username))
                    print('用户目录创建成功！')
                except Exception as e:
                    print('用户创建目录失败！', e)
        else:
            print('用户名重复，信息未保存')

    def change_userinfo(self, username): # 修改用户信息
        query_result = core.common.query_user(username) # 检测用户是否存在，不存在不处理
        if query_result != None:
            filename = query_result['filename']
            userinfo = query_result['content']
            print('before update:', userinfo)
            update_item = input('请输入要修改的项目，例如password，phonenumber，spacesize，level：')
            if update_item in ('username', 'id'):
                print(update_item, '项不可更改')
            elif update_item in ('password', 'phonenumber', 'spacesize', 'level'):
                print('update item: %s' % update_item)
                update_value = input('请输入要修改的项目的新值：')
                if update_item == 'password':
                    userinfo[update_item] = hashmd5(update_value)
                else:
                    userinfo[update_item] = update_value
                with open(os.path.join(core.settings.userinfo_dir, filename), 'w', encoding='utf-8') as f:
                    json.dump(userinfo, f)
                    print(update_item, '项用户信息变更保存完毕')
                    print('after update:', userinfo)
            else:
                print('输入信息错误,', update_item, '项不存在')
        else:
            print('用户不存在，无法修改')

    def delete_user(self, username):
        query_result = core.common.query_user(username) # 检测用户是否存在，不存在不处理
        if query_result != None:
            filename = query_result['filename']
            userfile_path = os.path.join(core.settings.userinfo_dir, filename)
            os.remove(userfile_path)
            query_result_again = core.common.query_user(username)
            if query_result_again == None:
                print('用户信息文件删除成功！')
                try:
                    shutil.rmtree(os.path.join(core.settings.file_dir, username))
                    print('用户家目录删除成功')
                except Exception as e:
                    print('用户家目录删除失败', e)
            else:
                print('用户信息文件删除失败！')
        else:
            print('用户不存在或者已经被删除')

    def query_all_user(self): # 查询所有用户信息，用于调试使用
        filelist = os.listdir(core.settings.userinfo_dir)
        if filelist != []:
            for filename in filelist:
                with open(os.path.join(core.settings.userinfo_dir, filename), 'rb') as f:
                    userinfo = json.load(f)
                    print(filename, userinfo)
        else:
            print('用户信息为空')

    def interactive(self):
        userpage = '''
        用户界面管理
            1、新增用户
            2、查询用户
            3、修改用户
            4、删除用户
            退出请按q
            返回上一界面请按r
        '''

        userpage_data = {
            '1':'save_userinfo',
            '2':'query_userinfo',
            '3':'change_userinfo',
            '4':'delete_user'
        }

        while True:
            print('\033[1;35m{}\033[0m'.format(userpage))
            choice = input('请输入你的选择：').strip()
            if choice == 'q':
                exit('退出程序！')
            elif choice == 'r':
                break
            elif choice in userpage_data:
                username = input('请输入用户名：').strip()
                if username == '':
                    print('用户不能为空')
                    continue
                if hasattr(self, userpage_data[choice]):
                    f = getattr(self, userpage_data[choice])
                    f(username)
            else:
                print('\033[1;31m输入错误，请重新输入\033[0m')
                continue