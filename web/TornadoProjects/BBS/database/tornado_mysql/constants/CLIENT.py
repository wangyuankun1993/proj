# -*- coding: utf-8 -*-
# Product Name: PyCharm
# Project Name: BBS
# File Name: CLIENT
# Date: 2022/01/15 19:37:48
# Author: wangyuankun
# Function: This file is to achieve CLIENT!
LONG_PASSWORD = 1
FOUND_ROWS = 1 << 1
LONG_FLAG = 1 << 2
CONNECT_WITH_DB = 1 << 3
NO_SCHEMA = 1 << 4
COMPRESS = 1 << 5
ODBC = 1 << 6
LOCAL_FILES = 1 << 7
IGNORE_SPACE = 1 << 8
PROTOCOL_41 = 1 << 9
INTERACTIVE = 1 << 10
SSL = 1 << 11
IGNORE_SIGPIPE = 1 << 12
TRANSACTIONS = 1 << 13
SECURE_CONNECTION = 1 << 15
MULTI_STATEMENTS = 1 << 16
MULTI_RESULTS = 1 << 17
CAPABILITIES = (LONG_PASSWORD | LONG_FLAG | TRANSACTIONS |
                PROTOCOL_41 | SECURE_CONNECTION)