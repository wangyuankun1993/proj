# -*- coding: utf-8 -*-
# Product Name: PyCharm
# Project Name: BBS
# File Name: logger
# Date: 2022/01/14 17:50:17
# Author: wangyuankun
# Function: This file is to achieve logger!
import logging
import logging.config
import functools
from conf import LOGGING

def logger(name): # 记录日志
    logging.config.dictConfig(LOGGING)
    try:
        log = logging.getLogger(name)
    except Exception as e:
        raise e
    return log