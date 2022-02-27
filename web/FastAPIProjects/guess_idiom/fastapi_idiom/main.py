# -*- coding: utf-8 -*-
# Product Name: PyCharm
# Project Name: guess_idiom
# File Name: main
# Date: 2022/01/16 19:33:54
# Author: wangyuankun
# Function: This file is to achieve main!
from fastapi import FastAPI, Header, HTTPException, Depends

from .models import models
from .models.database import engine
from .routers import users, games
from .utils.user_auth import auth_token

models.Base.metadata.create_all(bind=engine) # 创建数据表
app = FastAPI() # 实例化FastAPI应用

async def get_token_header(authorization: str = Header(...)):
    """
    获取Token并验证
    :param authorization:
    :return: openid
    """
    token = authorization.split(' ')[-1] # 获取token
    openid = auth_token(token) # 验证token
    if not openid:
        raise HTTPException(status_code=400, detail="无效Token")

# 用户相关路由
app.include_router(
    users.router,
    prefix='/api/users',
)

# 游戏和相关路由
app.include_router(
    games.router,
    prefix='/api/games',
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)