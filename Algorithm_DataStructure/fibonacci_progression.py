# -*- coding:utf-8 -*-
# Product Name: PyCharm
# Project Name: proj
# File Name: fibonacci_progression.py
# Date: 2022/02/01 01:01:33
# Author: wangyuankun
# Function: This file is to achieve xxx function!
from progression import Progression

class FibonacciProgression(Progression):
    def __init__(self, first=0, second=1):
        super().__init__(first)
        self._prev = second - first

    def _advance(self):
        self._prev, self._current = self._current, self._prev + self._current
