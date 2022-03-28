# -*- coding: utf-8 -*-
# Product Name: PyCharm
# Project Name: LeetCode
# File Name: twoSum_hash.py
# Date: 2022/03/04 00:24:57
# Author: wangyuankun
# Function: This file is to achieve twoSum_hash function.
from typing import List
class Solution():
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = dict()
        for i, num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target - num], i]
            hashtable[nums[i]] = i
        return []