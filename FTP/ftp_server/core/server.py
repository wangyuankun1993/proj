# -*- coding: utf-8 -*-
# Product Name: PyCharm
# Project Name: wangyuankun
# File Name: server.py
# Date: 2021/6/17 23:55:29
# Author: wangyuankun
# Function: This file is to achieve server program !
import socketserver, sys, json, os, time, shutil
import core.common

def processbar(part, total): # 进度条，运行会导致程序变慢
    if total != 0:
        done = int(50 * part / total)
        sys.stdout.write('\r[%s%s]' % ('■' * done, '  ' * (50 - done))) # 注意：一个方块对应2个空格
        sys.stdout.write('{:.2%}'.format(part / total) + ' ' * 3 + str(part) + '/' + str(total))
        sys.stdout.flush()

def timestamp_to_formatstringtime(timestamp): # 时间戳转化为格式化的字符串
    structtime = time.localtime(timestamp)
    formatstringtime = time.strftime('%Y%m%d %H:%M:%S', structtime)
    return formatstringtime

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        auth_tag = False
        while auth_tag != True:
            auth_result = self.auth() # 用户认证，如果通过，返回用户名，不通过为None
            print('the authentication result is:', auth_result)
            if auth_result != None:
                self.username = auth_result['content']['username']
                self.spacesize = auth_result['content']['spacesize']
                auth_tag = True
                print(self.username, self.spacesize)
                user_homedir = os.path.join(core.settings.file_dir, self.username)
                if os.path.isdir(user_homedir):
                    self.position = user_homedir # 定锚，用户家目录
                    print(self.position)

        while True:
            print('当前连接:', self.client_address)
            self.data = self.request.recv(1024).strip()
            print(self.data.decode())
            if not self.data:
                print(self.client_address, '断开了')
                break
            cmd_dic = json.loads(self.data.decode('utf-8'))
            action = cmd_dic['action']
            if hasattr(self, action):
                func = getattr(self, action)
                func(cmd_dic)
            else:
                print('未支持指令：', action)

    def auth(self): # 用户认证
        self.data = json.loads(self.request.recv(1024).decode('utf-8'))
        print(self.data)
        recv_username = self.data['username']
        recv_password = self.data['password']
        query_result = core.common.query_user(recv_username)
        print(query_result)
        if query_result == None:
            self.request.send(b'user does not exist')
        elif query_result['content']['password'] == recv_password:
            self.request.send(b'ok')
            return query_result # 返回查询结果
        elif query_result['content']['password'] != recv_password:
            self.request.send(b'password error')
        else:
            self.request.send(b'unknown error')

    def pwd(self, *args): # 查看当前目录
        current_position = self.position
        result = current_position.replace(core.settings.file_dir, '') # 截断目录信息，使用户只能看到自己的家目录
        print(result)
        self.request.send(json.dumps(result).encode('utf-8'))

    def ls(self, *args): # 列出当前目录下的所有文件信息，类型，字节数，生成时间
        result = ['%s-20s%-7s%-10s%-23s' % ('filename', 'type', 'bytes', 'creationtime')] # 信息标题
        for f in os.listdir(self.position):
            f_abspath = os.path.join(self.position, f) # 给出文件的绝对路径，不然程序会找不到文件
            if os.path.isdir(f_abspath):
                type = 'd'
            elif os.path.isfile(f_abspath):
                type = 'f'
            else:
                type = 'unknown'
            fsize = os.path.getsize(f_abspath)
            ftime = timestamp_to_formatstringtime(os.path.getctime(f_abspath))
            result.append('%-20s%-7s%-10s%-23s' % (f, type, fsize, ftime))
        self.request.send(json.dumps(result).encode('utf-8'))

    def du_calc(self): # 注意不能使用os.paht.getsize('D:\python-study\s14') 返回的是所有目录大小的和
        '''统计纯文件和目录占用空间大小，结果小于再os上使用du -s查询，因为有一些（例如'.','..'）隐藏文件包含在内'''
        totalsize = 0
        if os.path.isdir(self.position):
            dirsize, filesize = 0, 0
            for root, dirs, files in os.walk(self.position):
                for d in dirs: # 计算目录占用空间，Linux中每个目录占用4096bytes，实际上也可以按这个值来相加
                    dirsize += os.path.getsize(os.path.join(root, d))
                for f in files: # 计算文件占用空间
                    filesize += os.path.getsize(os.path.join(root, f))
            totalsize = dirsize + filesize
            return totalsize

    def du(self, *args): # 查看当前目录大小
        totalsize = self.du_calc()
        result = 'current directory total sizes: %d' % totalsize
        print(result)
        self.request.send(json.dumps(result).encode('utf-8'))
        return totalsize

    def cd(self, *args): # 切换目录
        print(*args)
        user_homedir = os.path.join(core.settings.file_dir, self.username)
        cmd_dic = args[0]
        error_tag = False
        '''判断目录信息'''
        if cmd_dic['dirname'] == '':
            self.position = user_homedir
        elif cmd_dic['dirname'] in ('.','/') or '//' in cmd_dic['dirname']: # '.','/','//','///+'匹配
            pass
        elif cmd_dic['dirname'] == '..':
            if user_homedir != self.position and user_homedir in self.position: # 当前目录不是家目录，并且当前目录是家目录下的子目录
                self.position = os.path.dirname(self.position)
        elif '.' not in cmd_dic['dirname'] and os.path.isdir(os.path.join(self.position, cmd_dir['dirname'])):
            self.position = os.path.join(self.position, cmd_dic['dirname'])
        else:
            error_tag = True

        if error_tag:
            result = 'Error, %s is not path here, or path does not exist!' % cmd_dic['dirname']
            self.request.send(json.dumps(result).encode('utf-8'))
        else:
            self.pwd()

    def mkdir(self, *args): # 创建目录
        try:
            dirname = args[0]['dirname']
            if dirname.isalnum(): # 判断文件是否只有数字和字母
                if os.path.exists(os.path.join(self.position, dirname)):
                    result = '%s have existed' % dirname
                else:
                    os.mkdir(os.path.join(self.position, dirname))
                    result = '%s created success' % dirname
            else:
                result = 'Illegal character %s, dirname can only by string and num here.' % dirname
        except TypeError:
            result = 'please input dirname'

        self.request.send(json.dumps(result).encode('utf-8'))

    def rm(self, *args): # 删除文件
        filename = args[0]['filename']
        confirm = args[0]['confirm']
        file_abspath = os.path.join(self.position, filename)
        if os.path.isfile(file_abspath):
            if confirm == True:
                os.remove(file_abspath)
                result = '%s have been deleted.' % filename
            else:
                result = 'Not file deleted'
        elif os.path.isdir(file_abspath):
            result = '%s is a dir, please use rmdir' % filename
        else:
            result = 'File %s not exist!' % filename
        self.request.send(json.dumps(result).encode('utf-8'))

    def rmdir(self, *args):
        dirname = args[0]['dirname']
        confirm = args[0]['confirm']
        dir_abspath = os.path.join(self.position, dirname)
        if '.' in dirname or '/' in dirname: # 不能跨目录删除
            result = 'should not rmdir %s this way' % dirname
        elif os.path.isdir(dir_abspath):
            if confirm == True:
                shutil.rmtree(dir_abspath)
                result = '%s have been deleted.' % dirname
            else:
                result = 'Not dir deleted.'
        elif os.path.isfile(dir_abspath):
            result = '%s is a file, please use rm' % dirname
        else:
            result = 'directory %s not exist!' % dirname
        self.request.send(json.dumps(result).encode('utf-8'))

    def mv(self, *args): # 实现功能：移动文件，移动目录，文件重命名，目录重命名
        try:
            print(args)
            objname = args[0]['objname']
            dstname = args[0]['dstname']
            obj_abspath = os.path.join(self.position, objname)
            dst_abspath = os.path.join(self.position, dstname)
            if os.path.isfile(obj_abspath):
                if os.path.isdir(dst_abspath) or not os.path.exists(dst_abspath):
                    shutil.move(obj_abspath, dst_abspath)
                    result = 'move success'
                elif os.path.isfile(dst_abspath):
                    result = 'moving cancel, file has been exist.'
            elif os.path.isdir(obj_abspath):
                if os.path.isdir(dst_abspath) or not os.path.exists(dst_abspath):
                    shutil.move(obj_abspath, dst_abspath)
                    result = 'move success'
                elif os.path.isfile(dst_abspath):
                    result = 'moving cancel, %s is a file.' % dst_abspath
            else:
                result = 'nothing done'
            self.request.send(json.dumps(result).encode('utf-8'))
        except Exception as e:
            print(e)
            result = 'moving fail,' + e
            self.request.send(json.dumps(result).encode('utf-8'))

    def get(self, *args): # 发送给客户端文件
        cmd_dic = args[0]
        filename = cmd_dic['filename']
        filepath = os.path.join(self.position, filename)
        if os.path.isfile(filepath):
            filesize = os.path.getsize(filepath)
            # 直接调用系统命令取得MD5值，如果使用hashlib，需要些open打开文件-》read读取文件（可能文件大会很耗时）-》m.update计算三步，代码量更多，效率也低
            # filemd5 = os.popen('md5sum %s' % filepath).read().split()p[0]
            filemd5 = 'a' # Windows测试用
            msg = {
                'action':'get',
                'filename':filename,
                'filemd5':filemd5,
                'override':'True'
            }
            self.request.send(json.dumps(msg).encode('utf-8'))
            '''接下来发送文件给客户端'''
            self.request.recv(1024) # 接收ACK信号，下一步发送文件
            f = open(filepath, 'rb')
            send_size = 0
            for line in f:
                send_size += len(line)
                self.request.send(line)
                processbar(send_size, filesize)
            else:
                print('文件传输完毕')
                f.close()
        else:
            print(filepath, '文件未找到')
            self.request.send(json.dumps('Filenotfound').encode('utf-8'))

    def put(self, *args): # 接收客户端文件
        cmd_dic = args[0]
        filename = os.path.basename(cmd_dic['filename']) # 传输进来的文件名可能带有路径，将路径去掉
        filesize = cmd_dic['filesize']
        filemd5 = cmd_dic['filemd5']
        override = cmd_dic['override']
        receive_size = 0
        file_path = os.path.join(self.position, filename)
        if override != 'True' and os.path.exists(file_path): # 检测文件是否已经存在
            self.request.send(b'file have exists, do nothing!')
        else:
            if os.path.isfile(file_path): # 如果文件已经存在，先删除，再计算磁盘空间大小
                os.remove(file_path)
            current_size = self.du() # 调用du查看用户磁盘空间大小，但是du命令的最后会发送一个结果信息给client，会和前面和后面的信息粘包，需要注意
            self.request.recv(1024) # 接收客户端ack信号，防止粘包，代号：P01
            print(self.spacesize, cueernt_size, filesize)
            if self.spacesize >= current_size + filesize:
                self.request.send(b'begin') # 发送开始传输信号
                f = open(file_path, 'wb')

                while filesize > receive_size:
                    if filesize - receive_size > 1024:
                        size = 1024
                    else:
                        size = filesize - receive_size
                    data = self.request.recv(size)
                    f.write(data)
                    receive_size += len(data)
                    processbar(receive_size, filesize) # 服务端打印进度条，不需要可以注释掉
                else:
                    print('file [%s] has uploaded...' % filename)
                    f.close()
                receive_filemd5 = os.popen('md5sum %s' % file_path).read().split()[0]
                receive_filemd5 = 'a' # Windows测试用
                print('\r\n', file_path, 'md5:', receive_md5, '原文件md5:', filemd5)
                if receive_filemd5 == filemd5:
                    self.request.send(b'file received successfully!')
                else:
                    self.request.send(b'Error, file received have problems!')
            else:
                self.request.send(b'Error, disk space do not enough! Nothing done! Total: %d, current: %d, rest:%d, filesize:%d' % (self.spacesize, current_size, self.spacesize - current_size, filesize))

    def newget(self, *args): # 发送给客户端文件，具有断点续传功能
        cmd_dic = args[0]
        filename = cmd_dic['filename']
        send_size = cmd_dic['filesize']
        print(filename)
        file_path = os.path.join(self.position, filename)
        if os.path.isfile(file_path):
            filesize = os.path.getsize(file_path)
            # 直接调用系统命令取得MD5值，如果使用hashlib，需要写open打开文件-》read读取文件（可能文件大会很耗时）-》m.updata计算三步，代码量更多，效率也低
            # filemd5 = os.popen('md5sum %s' % file_path).read().split()[0]
            filemd5 = 'a' # Windows测试用
            msg = {
                'action':'newget',
                'filename':filename,
                'filesize':filesize,
                'filemd5':filemd5
            }
            print(msg)
            self.request.send(json.dumps(msg).encode('utf-8'))
            self.request.recv(1024) # 接收ACK信号，下一步发送文件
            f = open(file_path, 'rb')
            f.seek(send_size, 0)
            for line in f:
                send_size += len(line)
                self.request.send(line)
                processbar(send_size, filesize)
            else:
                print('文件传输完毕')
                f.close()
        else:
            print(file_path, '文件未找到')
            self.request.send(json.dumps('Filenotfound').encode('utf-8'))

    def newput(self, *args): # 接收客户端文件，具有断点续传功能
        cmd_dict = args[0]
        filename = os.path.basename(cmd_dict['filename']) # 传输进来的文件名可能带有路径，将路径去掉
        filesize = cmd_dict['filesize']
        filemd5 = cmd_dict['filemd5']
        tag = cmd_dictp['tag']
        receive_size = 0
        file_path = os.path.join(self.position, filename)
        if os.path.isfile(file_path): # 检测文件是否已经存在
            self.request.send('文件存在'.encode())
            tag = self.request.recv(1024).decode() # 接收客户端ack信号
            if tag == 'o':
                os.remove(file_path) # 如果文件已经存在，先删除，再计算磁盘空间大小
                self.upload(tag, filename, filemd5, filesize, file_path, receive_size)
            elif tag == 'r':
                exist_file_size = os.path.getsize(file_path)
                if exist_file_size <= filesize:
                    receive_size = exist_file_size
                    self.upload(tag, filename, filemd5, filesize, file_path, receive_size)
                else:
                    print('服务器已存在同名文件且比原文件大')
                    msg = {
                        'content':'服务器已存在同名文件且比原文件大'
                    }
                    self.request.send(json.dumps(msg).encode('utf-8'))
            else:
                msg = {
                    'content':'文件未上传'
                }
                self.request.send(json.dumps(msg).encode('utf-8'))
        else: # 文件不存在：如果文件不存在的话，就不用管tag了，直接计算磁盘空间，然后上传
            self.request.send('文件不存在！'.encode())
            tag = self.request.recv(1024).decode() # 接收客户端ack信号
            self.upload(tag, filename, filemd5, filesize, file_path, receive_size)

    def upload(self, tag, filename, filemd5, filesize, file_path, receive_size):
        current_size = self.du_calc()
        print('用户总空间：', self.spacesize, '目前剩余空间：', current_size, '文件大小：', fielsize)
        if tag == 'r':
            needrecv_size = filesize - receive_size
        else:
            needrecv_size = filesize
        if self.spacesize >= current_size + needrecv_size:
            msg = {
                'position':receive_size,
                'content':'begin'
            }
            self.request.send(json.dumps(msg).encode('utf-8')) #　发送开始传输信号
            if tag == 'r':
                f = open(file_path, 'ab')
            else:
                f = open(file_path, 'wb')
            while filesize > receive_size:
                if filesize - receive_size > 1024:
                    size = 1024
                else:
                    size = filesize - receive_size
                data = self.request.recv(size)
                f.write(data)
                receive_size += len(data)
                processbar(receive_size, filesize) # 服务端进度条，不需要可以注释掉
            f.close()
            receive_filemd5 = 'a'
            print('\r\n', filename, 'md5:', receive_filemd5, '原文件md5:', filemd5)
            if receive_filemd5 == filemd5:
                self.request.send(b'file received successfully!')
            else:
                self.request.send(b'Error, file received have problems!')
        else:
            msg = {
                'content':'Error, disk space do not enough! Nothing done! Total: %d, current: %d, rest: %d, filesize: %d' % (
                    self.spacesize, current_size, self.spacesize - current_size, filesize
                )
            }
            self.request.send(json.dumps(msg).encode('utf-8'))