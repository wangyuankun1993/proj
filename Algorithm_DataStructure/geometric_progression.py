# -*- coding:utf-8 -*-
# Product Name: PyCharm
# Project Name: proj
# File Name: geometric_progression.py
# Date: 2022/02/01 00:48:12
# Author: wangyuankun
# Function: This file is to achieve xxx function!
from progression import Progression

class GeometricProgression(Progression):
    def __init__(self, base=2, start=1):
        super().__init__(start)
        self._base = base

    def _advance(self):
        self._current *= self._base
