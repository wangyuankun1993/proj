# -*- coding:utf-8 -*-
# Product Name: PyCharm
# Project Name: proj
# File Name: score_board.py
# Date: 2022/02/02 20:52:42
# Author: wangyuankun
# Function: This file is to achieve xxx function!
class Scoreboard():
    """Fixed-length sequence of high scores in nondecreasing order."""
    def __init__(self, capacity=10):
        """Initialize scoreboard with given maximum capacity."""
        self._board = [None] * capacity
        self._n = 0

    def __getitem__(self, k):
        """Return entry at index k."""
        return self._board[k]

    def __str__(self):
        return '\n'.join(str(self._board[j]) for j in range(self._n))

    def add(self, entry):
        score = entry.get_score()
        good = self._n < len(self._board) or score > self._board[-1].get_score()
        if good:
            if self._n < len(self._board):
                self._n += 1
            j = self._n - 1
            while j > 0 and self._board[j-1].get_score() < score:
                self._board[j] = self._board[j-1]
                j -= 1
            self._board[j] = entry
