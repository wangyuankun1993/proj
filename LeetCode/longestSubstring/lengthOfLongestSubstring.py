# -*- coding: utf-8 -*-
# Product Name: PyCharm
# Project Name: LeetCode
# File Name: lengthOfLongestSubstring.py
# Date: 2022/03/06 15:41:23
# Author: wangyuankun
# Function: This file is to achieve lengthOfLongestSubstring function.
class Solution():
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        start = 0
        dict1 = {}
        for i in range(len(s)):
            current = s[i]
            if current not in dict1.keys():
                dict1[current] = i
            else:
                if dict1[current] + 1 > start:
                    start = dict1[current] + 1
                dict1[current] = i
            if i - start + 1 > length:
                length = i - start + 1
        return length