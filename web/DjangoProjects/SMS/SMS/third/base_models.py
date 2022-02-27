# -*- coding: utf-8 -*-
# Product Name: PyCharm
# Project Name: SMS
# File Name: base_models
# Date: 2022/01/14 10:10:48
# Author: wangyuankun
# Function: This file is to achieve base models!

from django.db import models

# Create your models here.
class CreateUpdateMixin(models.Model):
    """
    模型创建和更新时间戳Mixin
    """
    status = models.BooleanField(default=True,help_text='状态',db_index=True) # 状态值
    created_at = models.DateTimeField(auto_now_add=True,editable=True,help_text='创建时间') # 创建时间
    updated_at = models.DateTimeField(auto_now=True,editable=True,help_text='更新时间') # 更新时间

    class Meta:
        abstract = True # 抽象类，只用作继承用，不会生成表