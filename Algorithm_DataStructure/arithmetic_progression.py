# -*- coding:utf-8 -*-
# Product Name: PyCharm
# Project Name: proj
# File Name: arithmetic_progression.py
# Date: 2022/02/01 00:30:39
# Author: wangyuankun
# Function: This file is to achieve xxx function!
from progression import Progression

class ArithmeticProgression(Progression):
    def __init__(self, increment=1, start=0):
        super().__init__(start)
        self._increment = increment

    def _advance(self):
        self._current += self._increment
