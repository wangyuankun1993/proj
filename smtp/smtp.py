# -*- coding:utf-8 -*-
# Product Name: PyCharm
# Project Name: proj
# File Name: smtp.py
# Date: 2022/02/19 15:43:10
# Author: wangyuankun
# Function: This file is to achieve xxx function!
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib

def _format_addr(s):
	name, addr = parseaddr(s)
	return formataddr((Header(name, 'utf-8').encode(), addr))

from_addr = input('From:')
password = input('Password:')
to_addr = input('To:')
smtp_server = input('SMTP server:')

msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
msg['From'] = _format_addr('Python amateur <%s>' % from_addr)
msg['To'] = _format_addr('Adminisstrtor <%s>' % to_addr)
msg['Subject'] = Header('Greeting from SMTP...', 'utf-8').encode()

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
