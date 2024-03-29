# -*- coding: utf-8 -*-
# Product Name: PyCharm
# Project Name: BBS
# File Name: tag_handlers
# Date: 2022/01/15 18:52:43
# Author: wangyuankun
# Function: This file is to achieve tag_handlers!
from tornado import gen

from handlers.base_handlers import BaseHandler
from database.sql_utils.tag import get_tag_list, get_all_tags

from utils.auth import login_required


class TagListHandler(BaseHandler):
    """
    标签列表控制器
    """
    @gen.coroutine
    @login_required
    def get(self, *args, **kwargs):  # 渲染页面
        data = yield get_tag_list()
        tags = yield get_all_tags()
        self.render('tag_list.html', data={'tag_list': data, 'tags': tags})