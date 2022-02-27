# -*- coding: utf-8 -*-
# Product Name: PyCharm
# Project Name: BBS
# File Name: _compat
# Date: 2022/01/15 17:39:46
# Author: wangyuankun
# Function: This file is to achieve _compat!
import sys

PY2 = sys.version_info[0] == 2
PYPY = hasattr(sys, 'pypy_translation_info')
JYTHON = sys.platform.startswith('java')
IRONPYTHON = sys.platform == 'cli'
CPYTHON = not PYPY and not JYTHON and not IRONPYTHON

if PY2:
    range_type = xrange
    text_type = unicode
    long_type = long
    str_type = basestring
else:
    range_type = range
    text_type = str
    long_type = int
    str_type = str