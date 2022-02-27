# -*- coding:utf-8 -*-
# Product Name: PyCharm
# Project Name: proj
# File Name: progression.py
# Date: 2022/02/01 00:00:20
# Author: wangyuankun
# Function: This file is to achieve xxx function!
class Progression():
    """
    Iterator producing a genic progression.
    """
    def __init__(self, start=0):
        """Initialize current to the first value of the progression."""
        self._current = start

    def _advance(self):
        """Update self._current to a new value."""
        self._current += 1

    def __next__(self):
        if self._current is None:
            raise StopIteration()
        else:
            answer = self._current
            self._advance()
            return answer

    def __iter__(self):
        """By convention, an iterator must return itsself as an iterator."""
        return self

    def print_progression(self, n):
        """Print next n values of the progression."""
        print(''.join(str(next(self)) for j in range(n)))
