# -*- coding: utf-8 -*-
# Product Name: PyCharm
# Project Name: LeetCode
# File Name: longestPalindrome.py
# Date: 2022/03/11 00:15:58
# Author: wangyuankun
# Function: This file is to achieve longestPalindrome function.
class Solution():
    def longestPalindrome(self, s: str) -> str:
        # 构建判定回文串函数
        is_palindromic_string = lambda s: s == s[::-1]
        max_len, max_substr = 0, ""
        if len(s) < 2:
            max_substr = s

        for i in range(len(s) - 1):
            for j in range(i + 1, len(s)):
                cur_substr = s[i: j + 1]
                print(cur_substr)
                if is_palindromic_string(cur_substr):
                    cur_len = len(cur_substr)
                    if cur_len > max_len:
                        max_len = cur_len
                        max_substr = cur_substr
        if max_substr == "":
            max_substr = s[0]
        return max_substr