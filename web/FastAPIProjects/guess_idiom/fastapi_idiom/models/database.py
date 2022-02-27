# -*- coding: utf-8 -*-
# Product Name: PyCharm
# Project Name: guess_idiom
# File Name: database
# Date: 2022/01/16 11:53:14
# Author: wangyuankun
# Function: This file is to achieve database!
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from fastapi_idiom.config import Config

engine = create_engine(Config.SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()