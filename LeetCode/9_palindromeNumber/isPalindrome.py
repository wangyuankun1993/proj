# -*- coding: utf-8 -*-
# Product Name: PyCharm
# Project Name: LeetCode
# File Name: isPalindrome.py
# Date: 2022/03/20 23:30:54
# Author: wangyuankun
# Function: This file is to achieve isPalindrome function.
class Solution():
    def isPalindrome(self, x: int) -> bool:
        str1 = str(x)
        if str1 == str1[::-1]:
            return True
        else:
            return False

obj = Solution()
result = obj.isPalindrome(0)
print(result)