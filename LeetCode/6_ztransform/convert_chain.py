# -*- coding: utf-8 -*-
# Product Name: PyCharm
# Project Name: LeetCode
# File Name: convert_chain.py
# Date: 2022/03/15 21:11:52
# Author: wangyuankun
# Function: This file is to achieve convert_chain function.
from itertools import chain


class Solution():
    def convert(self, s: str, numRows: int) -> str:
        r = numRows
        if r < 1 or r >= len(s):
            return s
        mat = [[] for _ in range(r)]
        t, x = r * 2 - 2, 0
        for i, ch in enumerate(s):
            mat[x].append(ch)
            x += 1 if i % t < r - 1 else -1
        return ''.join(chain(*mat))

obj = Solution()
result = obj.convert("abcdefghigklmn", 3)
print(result)