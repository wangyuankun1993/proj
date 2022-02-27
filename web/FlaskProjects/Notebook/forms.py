# -*- coding: utf-8 -*-
# Product Name: PyCharm
# Project Name: Notebook
# File Name: forms
# Date: 2022/01/11 17:39:56
# Author: wangyuankun
# Function: This file is to achieve forms!
from wtforms import Form, StringField, TextAreaField, PasswordField
from wtforms.validators import DataRequired, Length, ValidationError
from flask_wtf import FlaskForm
from mysql_util import MysqlUtil

# 创建登录表单类
class LoginForm(FlaskForm):
    username = StringField(
        '用户名',
        validators=[
            DataRequired(message='请输入用户名'),
            Length(min=4,max=25,message='长度在4-25个字符之间')
        ]
    )
    password = PasswordField(
        '密码',
        validators=[
            DataRequired(message='密码不能为空'),
            Length(min=6,max=20,message='长度在6-20个字符之间')
        ]
    )

    def validate_username(self,field):
        # 根据用户名查找user表中记录
        sql = "SELECT * FROM users WHERE username='%s'" % field.data
        db = MysqlUtil() # 实例化数据库操作类
        result = db.fetchone(sql) # 获取一条记录
        if not result:
            raise ValidationError("用户名不存在")

# 创建博客表单类
class ArticleForm(Form):
    title = StringField(
        '标题',
        validators=[
            DataRequired(message='长度在2-30个字符'),
            Length(min=2,max=30)
        ]
    )
    content = TextAreaField(
        '内容',
        validators=[
            DataRequired(message='长度不少于5个字符'),
            Length(min=5)
        ]
    )