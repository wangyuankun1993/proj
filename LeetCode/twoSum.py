# -*- coding: utf-8 -*-
# Product Name: PyCharm
# Project Name: LeetCode
# File Name: twoSum.py
# Date: 2022/03/03 23:49:08
# Author: wangyuankun
# Function: This file is to achieve twoSum function.
from typing import List
class Solution():
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        for i in range(length-1):
            for j in range(i+1, length):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []