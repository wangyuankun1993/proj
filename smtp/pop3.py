# -*- coding:utf-8 -*-
# Product Name: PyCharm
# Project Name: proj
# File Name: pop3.py
# Date: 2022/02/19 16:42:39
# Author: wangyuankun
# Function: This file is to achieve xxx function!
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr

import poplib

email = input('Email:')
password = input('Password:')
pop3_server = input('POP3 server:')

server = poplib.POP3(pop3_server)
server.set_debuglevel(1)
print(server.getwelcome().decode('utf-8'))

server.user(email)
server.pass_(password)

print('Message:%s. Size:%s' % server.stat())
resp, mails, octets = server.list()
print(mails)

index = len(mails)
resp, lines, octets = server.retr(index)

msg_content = b'\r\n'.join(lines).decode('utf-8')
msg = Parse().parsestr(msg_content)

server.quit()
