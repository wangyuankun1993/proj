# -*- coding: utf-8 -*-
# Product Name: PyCharm
# Project Name: BBS
# File Name: connect
# Date: 2022/01/15 17:34:12
# Author: wangyuankun
# Function: This file is to achieve connect!
from database import tornadoredis

from conf import REDIS


CONF = REDIS.get('default', {})
CONNECTION_POOL = tornadoredis.ConnectionPool(max_connections=500,wait_for_available=True)


def redis_connect():  # 异步连接redis
    return tornadoredis.Client(**CONF, connection_pool=CONNECTION_POOL)
