# -*- coding: utf-8 -*-
# Product Name: PyCharm
# Project Name: LeetCode
# File Name: convert.py
# Date: 2022/03/14 22:32:17
# Author: wangyuankun
# Function: This file is to achieve convert function.
class Solution():
    def convert(self, s: str, numRows: int) -> str:
        n, r = len(s), numRows
        if r == 1 or r >= n:
            return s
        t = r * 2 - 2
        c = (n + t - 1) // t * (r - 1)
        mat = [[''] * c for _ in range(r)]
        x, y = 0, 0
        for i, ch in enumerate(s):
            mat[x][y] = ch
            if i % t < r - 1:
                x += 1 # 向下移动
            else:
                x -= 1
                y += 1 # 向上移动
        return ''.join(ch for row in mat for ch in row if ch)

obj = Solution()
result = obj.convert("abcdefghigklmn", 3)
print(result)