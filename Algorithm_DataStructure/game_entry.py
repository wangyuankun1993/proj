# -*- coding:utf-8 -*-
# Product Name: PyCharm
# Project Name: proj
# File Name: game_entry.py
# Date: 2022/02/02 20:44:11
# Author: wangyuankun
# Function: This file is to achieve xxx function!
class GameEntry():
    """Represents one entry of a list of high scores."""
    def __init__(self, name, score):
        self._name = name
        self._score = score

    def get_name(self):
        return self._name

    def get_score(self):
        return self._score

    def __str__(self):
        return '{0}, {1}'.format(self._name, self._score)
