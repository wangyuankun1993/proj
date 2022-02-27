# -*- coding: utf-8 -*-
# Product Name: PyCharm
# Project Name: wangyuankun
# File Name: client.py
# Date: 2021/6/14 16:11:56
# Author: wangyuankun
# Function: This file is to achieve client !
import socket, os, json, hashlib, sys, time, getpass, logging
import core.settings

def hashmd5(*args): # MD5加密
    m = hashlib.md5()
    m.update(str(*args).encode())
    ciphertexts = m.hexdigest() # 密文
    return ciphertexts

def processbar(part, total): # 进度条，运行会导致程序变慢
    if total != 0:
        done = int(50 * part / total)
        sys.stdout.write("\r[%s%s]" % ('■' * done, '  ' * (50 - done))) # 注意：1个方块对应2个空格
        sys.stdout.write('{:.2%}'.format(part / total) + '' * 3 + str(part) + '/' + str(total))
        sys.stdout.flush()

class FtpClient(object):
    def __init__(self):
        self.client = socket.socket()

    def connect(self, ip, port): # 连接
        self.client.connect(ip, port)

    def auth(self): # 用户认证
        username = input('请输入用户名>>>:').strip()
        # password = getpass.getpass("请输入密码:").strip() # 在linux上输入密码不显示，此模块在pycharm中无法使用
        password = input('请输入密码>>>:').strip() # Windows测试用
        password = hashmd5(password)
        msg = {
            'username':username,
            'password':password
        }
        self.client.send(json.dumps(msg).encode('utf-8'))
        server_response = self.client.recv(1024).decode('utf-8')
        logging.info(server_response)
        if server_response == 'ok':
            print('认证通过！')
            return True
        else:
            print(server_response)
            return False

    def interactive(self): # 交互
        while True:
            self.pwd('pwd') # 打印家目录
            cmd = input('>>').strip()
            if len(cmd) == 0:
                continue
            cmd_str = cmd.split()[0] # 用户输入的第一个值必定是命令
            if hasattr(self, cmd_str): # 反射：判断一个对象中是否有字符串对应的方法或属性
                func = getattr(self, cmd_str) # 利用发射来解耦：根据字符串去获取对象里对应的方法的内存地址或对应属性的值
                func(cmd) # 调用命令对应的方法
            else:
                self.help()

    def help(self): # 帮住
        msg = '''
        仅支持如下命令：
        ls
        du
        pwd
        cd dirname/cd ./cd ..
        mkdir dirname
        rmdir dirname
        mv filename/dirname filename/dirname
        get filename [True] (True代表覆盖)
        put filename [True] (True代表覆盖)
        newget filename [o/r] (后续增加的新功能，支持断点续传，o代表覆盖，r代表断点续传)
        newput filename [o/r] (后续增加的新功能，支持断点续传，o代表覆盖，r代表断点续传)
        '''
        print(msg)

    def pwd(self, *args): # 查看当前目录
        cmd_split = args[0].split()
        if len(cmd_split) == 1:
            msg = {'action':'pwd'}
            self.exec_linux_cmd(msg)
        else:
            self.help()

    def ls(self, *args): # 文件浏览
        cmd_split = args[0].split()
        if len(cmd_split) == 1:
            msg = {'action','ls'}
            self.exec_linux_cmd(msg)
        else:
            self.help()

    def du(self, *args): # 查看当前目录大小
        cmd_split = args[0].split()
        if len(cmd_split) == 1:
            msg = {'action','du'}
            self.exec_linux_cmd(msg)
        else:
            self.help()

    def cd(self, *args): # 切换目录
        cmd_split = args[0].split()
        if len(cmd_split) == 1:
            dirname = ''
        elif len(cmd_split) == 2:
            dirname = cmd_split[1]
        else:
            self.help()

        msg = {
            'action':'cd',
            'dirname':dirname
        }
        self.exec_linux_cmd(msg)

    def mkdir(self, *args): # 生成目录
        cmd_split = args[0].split()
        if len(cmd_split) == 2:
            dirname = cmd_split[1]
            msg = {
                'action':'mkdir',
                'dirname':dirname
            }
            self.exce_linux_cmd(msg)
        else:
            help()

    def rm(self, *args): # 删除文件
        cmd_split = args[0].split()
        if len(cmd_split) == 2:
            filename = cmd_split[1]
            msg = {
                'action':'rm',
                'filename':filename,
                'confirm':True # 确认是否直接删除标志
            }
            self.exec_linux_cmd(msg)
        else:
            help()

    def rmdir(self, *args): # 删除目录
        cmd_split = args[0].split()
        if len(cmd_split) == 2:
            dirname = cmd_split(1)
            msg = {
                'action':'rmdir',
                'dirname':dirname,
                'confirm':True # 确认是否直接删除标志
            }
            self.exec_linux_cmd(msg)
        else:
            help()

    def mv(self, *args): # 实现功能：移动文件，移动目录，文件重命名，目录重命名
        cmd_split = args[0]split()
        if len(cmd_split) == 3:
            objname = cmd_split[1]
            dstname = cmd_split[2]
            msg = {
                'action':'mv',
                'objname':ojbname,
                'dstname':dstname
            }
            self.exec_linux_cmd(msg)
        else:
            help()

    def exec_linux_cmd(self, dict): # 用于后面调用linux命令
        logging.info(dict) # 将发送给服务端的命令保存到日志中
        self.client.send(json.dumps(dict).encode('utf-8'))
        server_response = json.loads(self.client.recv(4096).decode('utf-8'))
        if isinstance(server_response, list): # 判断是否为list类型
            for i in server_response:
                print(i)
        else:
            print(server_response)

    def get(self, *args): # 下载文件
        cmd_split = args[0].split()
        override = cmd_split[-1] # override：是否覆盖参数，True表示覆盖，放在最后一位
        if override != 'True':
            override = 'False'
        if len(cmd_split) > 1:
            filename = cmd_split[1]
            filepath = os.path.join(core.settings.download_dir, filename)
            if override != 'True' and os.path.isfile(filepath): # 判断下载目录是否已存在同名文件
                override_tag = input('文件已存在，要覆盖文件请输入yes >>>:').strip()
                if override_tag == 'yes':
                    self.put('put %s True' % filename)
                else:
                    print('下载取消')
            else:
                msg = {
                    'action':'get',
                    'filename':filename,
                    'filesize':0,
                    'filemd5':'',
                    'override':'True'
                }
                # logging.info(msg)
                self.client.send(json.dumps(msg).encode('utf-8'))
                server_response = json.loads(self.client.recv(1024).decode('utf-8'))
                logging.info(server_response)
                if server_response == 'Filenotfound':
                    print('File no found!')
                else:
                    print(server_response)
                    self.client.send(b'client have been ready to receive') # 发送信号，防止粘包
                    filesize = server_response['filesize']
                    filemd5 = server_response['filemd5']
                    receive_size = 0
                    f = open(filepath, 'wb')
                    while filesize > receive_size:
                        if filesize - receive_size > 1024:
                            size = 1024
                        else:
                            size = filesize - receive_size
                        data = self.client.recv(size)
                        f.write(data)
                        receive_size += len(data)
                        processbar(receive_size, filesize) # 打印进度条
                    f.close()
                    # receive_filemd5 = os.popen('md5sum %s' % filepath).read().split()[0]
                    receive_filemd5 = 'a' # Windows测试用
                    print('\r\n', filename, 'md5:', receive_filemd5, '源文件md5:', filemd5)
                    if receive_filemd5 == filemd5:
                        print('文件接收完成！')
                    else:
                        print('Error,文件接受异常！')
        else:
            help()

    def put(self, *args): # 上传文件
        cmd_split = args[0].split()
        override = cmd_split[-1] # override：是否覆盖参数，True表示覆盖，放在最后一位
        if override != 'True':
            override = 'False'

        if len(cmd_split) > 1:
            filename = cmd_split[1]
            filepath = os.path.join(core.settings.download_dir, filename)
            if os.path.isfile(filepath):
                filesize = os.path.getsize(filepath)

                # 直接调用系统命令取得MD5值，如果使用hashlib，需要写open打开文件-》read读取文件（可能文件大会很耗时）-》m.update计算三步，代码量更多，效率也低
                # filemd5 = os.popen('md5sum %s' % filepath).read().split()[0]
                filemd5 = 'a' # Windows测试

                msg = {
                    'action':'put',
                    'filename':filename,
                    'filesize':filesize,
                    'filemd5':filemd5,
                    'override':override
                }
                # logging.info(msg)
                self.client.send(json.dumps(msg).encode('utf-8'))
                # 防止粘包，等服务器确认：这里最好列出一些标准请求码，告诉客户端是否有权限传输文件，类似200 403等
                server_response = self.client.recv(1024)
                # logging.info(server_response)
                if server_response == b'file have exists, do nothing!':
                    override_tag = input('文件已存在，要覆盖文件请输入yes >>>:')
                    if override_tag == 'yes':
                        self.put('put %s True' % filename)
                    else:
                        print('文件未上传')
                else:
                    self.client.send(b'client have ready to send') # 发送确认信号，防止粘包，代号：P01
                    server_response = self.client.recv(1024).decode('utf-8')
                    print(server_response) # 注意：用于打印服务器反馈信息，例如磁盘空间不足信息，不能取消
                    if server_response == 'begin':
                        f = open(filepath, 'rb')
                        send_size = 0
                        for line in f:
                            send_size += len(line)
                            self.client.send(line)
                            processbar(send_size, filesize)
                        else:
                            print('\r\n', 'file upload success...')
                            f.close()
                            server_response = self.client.recv(1024).decode('utf-8')
                            print(server_response)
            else:
                print(filename, 'is not exist')
        else:
            self.help()

    def newget(self, *args): # 下载文件，具有断点续传功能
        cmd_split = args[0].split()
        tag = cmd_split[-1] # tag:o代表覆盖，r代表续传，放在最后一位

        if len(cmd_split) > 1:
            filename = cmd_split[1]
            filepath = os.path.join(core.settings.download_dir, filename)
            if tag not in ('o', 'r'):
                if os.path.isfile(filepath): # 判断下载目录是否已存在同名文件
                    tag = input('文件已存在，要覆盖文件请输入o，要断点续传请输入r>>>:').strip()
                else:
                    tag = 'o'

            if tag in ('o', 'r'):
                if tag == 'r':
                    local_filesize = os.path.getsize(filepath)
                else:
                    local_filesize = 0 # 本地文件大小

                msg = {
                    'action':'newget',
                    'filename':filename,
                    'filesize':local_filesize,
                    'filemd5':''
                }
                logging.info(msg)
                self.client.send(json.dumps(msg).encode('utf-8'))
                server_response = json.loads(self.client.recv(1024).decode('utf-8'))
                logging.info(server_response)
                if server_response == 'Filenotfound':
                    print('File no found!')
                else:
                    print(server_response)
                    self.client.send(b'client have been ready to receive') # 发送信号，防止粘包
                    filesize = server_response['filesize']
                    filemd5 = server_response['filemd5']
                    receive_size = local_filesize
                    if tag == 'r':
                        f = open(filepath, 'ab+') # 用于断点续传
                    else:
                        f = open(filepath, 'wb+') # 用于覆盖或者新生成文件
                    while filesize > receive_size:
                        if filesize - receive_size > 1024:
                            size = 1024
                        else:
                            size = filesize - receive_size
                        data = self.client.recv(size)
                        f.write(data)
                        receive_size += len(data)
                        processbar(receive_size, filesize) # 打印进度条
                    f.close()
                    # receive_filemd5 = os.popen('md5sum %s' % filepath).read().split()[0]
                    receive_filemd5 = 'a' # Windows测试用
                    print('\r\n', filename, 'md5:', receive_filemd5, '源文件md5:', filemd5)
                    if receive_filemd5 == filemd5:
                        print('文件接收完成！')
                    else:
                        print('Error,文件接受异常！')
            else:
                print('文件未下载')
        else:
            help()

    def newput(self, *args): # 上传文件，具有断点续传功能
        cmd_split = args[0].split()
        tag = cmd_split[-1] # tag：r代表续传，o代表覆盖，放在最后一位
        if tag not in ('o', 'r'):
            tag = 'unknown'

        if len(cmd_split) > 1:
            filename = cmd_split[1]
            filepath = os.path.join(core.settings.download_dir, filename)
            if os.path.isfile(filepath):
                filesize = os.path.getsize(filepath)
                # filesize = os.stat(filepath).st_size

                # 直接调用系统命令取得MD5值，如果使用hashlib，需要写open打开文件-》read读取文件（可能文件大会很耗时）-》m.updata计算三步，代码量更多，效率更低
                # filemd5 = os.popen('md5sum %s' % filepath).read().split()[0]
                filemd5 = 'a' # Windows测试
                msg = {
                    'action':'newput',
                    'filename':filename,
                    'filesize':filesize,
                    'filemd5':filemd5,
                    'tag':tag
                }
                # logging.info(msg)
                self.client.send(json.dumps(msg).encode('utf-8')) # 发送msg
                server_response1 = self.client.recv(1024).decode('utf-8') # 接收文件存在或者文件不存在
                # logging.info(server_response)
                print(server_response1)
                if server_response1 == '文件存在': # 再确认一遍tag
                    if tag == 'unknown':
                        tag = input('文件已存在，要覆盖文件请输入o，要断点传输请输入r>>>:').strip()
                        if tag not in ('o', 'r'):
                            tag = 'unknown'
                else: # 文件不存在时
                    tag = 'o'

                self.client.send(tag.encode())
                server_response2 = json.loads(self.client.recv(1024).decode('utf-8'))
                content = server_response2['content']

                if tag == 'o' or tag == 'r':
                    if content == 'begin':
                        position = server_response2['position']
                        print(position)
                        f = open(filepath, 'rb')
                        f.seek(position, 0)
                        send_size = position
                        for line in f:
                            send_size += len(line)
                            self.client.send(line)
                            processbar(send_size, filesize)
                        else:
                            print('\n', 'file upload success...')
                            f.close()
                            server_response3 = self.client.recv(1024).decode('utf-8') # 服务端对比md5后发送是否成功接收文件，成功或失败
                            print(server_response3)
                    else:
                        print(content) # content:服务器已存在同名文件
                else:
                    print(content) # content:文件未上传
            else:
                print(filename, 'is not exist')
        else:
            self.help()

    def close(self):
        self.client.close()