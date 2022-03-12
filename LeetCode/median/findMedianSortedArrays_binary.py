# -*- coding: utf-8 -*-
# Product Name: PyCharm
# Project Name: LeetCode
# File Name: findMedianSortedArrays_binary.py
# Date: 2022/03/09 23:00:16
# Author: wangyuankun
# Function: This file is to achieve findMedianSortedArrays_binary function.
from typing import List
class Solution():
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def getKthElement(k):
            """
            - 主要思路：要找到第k(k>twoSum)小的元素，要么就取pivot1 = nums1[k/addTwoNumbers-twoSum]和pivot2 = nums2[k/addTwoNumbers-twoSum]进行比较
            - 这里的“/”表示整除
            - nums1中小于等于pivot1的元素有nums1[0...k/addTwoNumbers-addTwoNumbers]共计k/addTwoNumbers-1个
            - nums2中小于等于pivot2的元素有nums2[0...k/addTwoNumbers-addTwoNumbers]共计k/addTwoNumbers-1个
            - 取pivot = min(pivot1, pivot2)，两个数组中小于等于pivot的元素共计不会超过(k/addTwoNumbers-twoSum)+(k/addTwoNumbers-twoSum)<=k-2个
            - 这样pivot本身最大也只能是第k-1小的元素
            - 如果pivot = pivot1，那么nums1[0...k/addTwoNumbers-twoSum]都不可能是第k小的元素。把这些元素全部“删除”，剩下的作为新的nums1数组
            - 如果pivot = pivot2，那么nums2[0...k/addTwoNumbers-twoSum]都不可能是第k小的元素。把这些元素全部“删除”，剩下的作为新的nums2数组
            - 由于我们“删除”了一些元素（这些元素都不第k小的元素要小），因此需要修改k的值，减去删除的数的个数
            :param k:
            :return:
            """
            index1, index2 = 0, 0
            while True:
                # 特殊情况
                if index1 == m:
                    return nums2[index2 + k - 1]
                if index2 == n:
                    return nums1[index1 + k - 1]
                if k == 1:
                    return min(nums1[index1], nums2[index2])

                # 正常情况
                newIndex1 = min(index1 + k//2 - 1, m - 1)
                newIndex2 = min(index2 + k//2 - 1, n - 1)
                pivot1, pivot2 = nums1[newIndex1], nums2[newIndex2]
                if pivot1 <= pivot2:
                    k -= newIndex1 - index1 + 1
                    index1 = newIndex1 + 1
                else:
                    k -= newIndex2 - index2 + 1
                    index2 = newIndex2 + 1
        m, n = len(nums1), len(nums2)
        totalLength = m + n
        if totalLength % 2 == 1:
            return getKthElement((totalLength + 1) // 2)
        else:
            return (getKthElement(totalLength // 2) + getKthElement(totalLength // 2 + 1)) / 2

obj = Solution()
result = obj.findMedianSortedArrays([1], [3,4])
print(result)