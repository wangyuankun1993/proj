# -*- coding: utf-8 -*-
# Product Name: PyCharm
# Project Name: LeetCode
# File Name: findMedianSortedArrays.py
# Date: 2022/03/06 22:22:15
# Author: wangyuankun
# Function: This file is to achieve findMedianSortedArrays function.
from typing import List
class Solution():
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = sorted(nums1 + nums2)
        if len(nums3) % 2 == 0:
            median = (nums3[int(len(nums3) / 2 - 1)] + nums3[int(len(nums3) / 2)]) / 2
        elif len(nums3) % 2 == 1:
            median = nums3[int((len(nums3) + 1) / 2) - 1]
        return median

obj = Solution()
result = obj.findMedianSortedArrays([1],[3,4])
print(result)