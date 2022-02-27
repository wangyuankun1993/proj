# -*- coding: utf-8 -*-
# Product Name: PyCharm
# Project Name: BBS
# File Name: conf
# Date: 2022/01/14 17:56:22
# Author: wangyuankun
# Function: This file is to achieve configuration!

import os

DOMAIN = 'http://127.0.0.1:9999'

DEFAULT_UPLOAD_PATH = os.path.join(os.path.dirname(__file__), 'pics')

SETTINGS = {
    'template_path': os.path.join(os.path.dirname(__file__), 'templates'),
    'static_path': os.path.join(os.path.dirname(__file__), 'static'),
    'cookie_secret': 'ZCSc6mcFTciwWc+WCGWt5xCnNUld0EJjs5GKaK2JTG8=',
    'login_url': '/auth/login',
    'xsrf_token': True,
    'debug': True
}

DATABASE = {
    'default': {
        'host': 'localhost',
        'port': 3306,
        'database': 'bbs',
        'user': 'root',
        'password': 'wangyuankun1993',
        'charset': 'utf8'
    }
}

REDIS = {
    'default': {
        'host': 'localhost',
        'port': 6379,
        'password': '',
        'selected_db': 0
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'format': '%(asctime)s [%(name)s:%(lineno)d] [%(levelname)s]- %(message)s'
    },
    'standard': {
        'format': '%(asctime)s [%(threadName)s:%(thread)d] [%(name)s:%(lineno)d] [%(levelname)s]- %(message)s'
    },
    'handlers': {
        'consloe': {
            'class': 'logging.StreamHandler',
            'level': 'INFO',
            'formatter': 'simple',
            'filename': os.path.join(os.path.dirname(__file__), 'bbs.log'),
            'mode': 'w+',
            'maxBytes': 1024*1024*5, # 5MB
            'backupCount': 20,
            'encoding': 'utf8'
        },
        'admin': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'DEBUG',
            'formatter': 'simple',
            'filename': os.path.join(os.path.dirname(__file__), 'admin.log'),
            'mode': 'w+',
            'maxBytes': 1024*1024*2,
            'backupCount': 20,
            'encoding': 'utf8'
        },
    },
    'loggers': {
        'console': {
            'level': 'INFO',
            'handlers': ['console'],
            'propagate': 'no'
        },
        'file': {
            'level': 'INFO',
            'handlers': ['file'],
            'propagate': 'no'
        },
        'admin': {
            'level': 'INFO',
            'handlers': ['admin'],
            'propagate': 'no'
        }
    }
}

try:
    from local_conf import *
except Exception as e:
    print("You should add an extra local_conf.py into this directory.")