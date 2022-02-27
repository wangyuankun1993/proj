# -*- coding: utf-8 -*-
# Product Name: PyCharm
# Project Name: BBS
# File Name: index_handlers
# Date: 2022/01/15 16:47:27
# Author: wangyuankun
# Function: This file is to achieve index handlers!
from tornado import gen

from handlers.base_handlers import BaseHandler

from database.sql_utils.tag import get_all_tags

class IndexHandler(BaseHandler):
    """
    首页控制器
    """
    @gen.coroutine
    def get(self, *args, **kwargs): # 渲染页面
        tags = yield get_all_tags() # 获取所有tag信息
        self.render('index.html', data={'tags':tags})