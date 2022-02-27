# -*- coding: utf-8 -*-
# Product Name: PyCharm
# Project Name: BBS
# File Name: util
# Date: 2022/01/15 18:00:08
# Author: wangyuankun
# Function: This file is to achieve util!
import struct

def byte2int(b):
    if isinstance(b, int):
        return b
    else:
        return struct.unpack("!B", b)[0]

def int2byte(i):
    return struct.pack("!B", i)

def join_bytes(bs):
    if len(bs) == 0:
        return ""
    else:
        rv = bs[0]
        for b in bs[1:]:
            rv += b
        return rv