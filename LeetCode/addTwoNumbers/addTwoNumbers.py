# -*- coding: utf-8 -*-
# Product Name: PyCharm
# Project Name: LeetCode
# File Name: addTwoNumbers.py
# Date: 2022/03/04 23:41:15
# Author: wangyuankun
# Function: This file is to achieve addTwoNumbers function.
# Definition for singly-linked list.
class ListNode():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(ListNode):
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = point = ListNode(0) # 将当前节点初始化为返回列表的哑节点
        carry = 0 # 将进位carry初始化为0
        while l1 or l2:
            new_point = ListNode(0)
            if not l1:
                sum_ = l2.val + carry
                new_point.val = sum_ % 10
                carry = sum_ // 10
                l2 = l2.next
            elif not l2:
                sum_ = l1.val + carry
                new_point.val = sum_ % 10
                carry = sum_ // 10
                l1 = l1.next
            else:
                sum_ = (l1.val + l2.val + carry)
                new_point.val = sum_ % 10
                carry = sum_ // 10
                l1 = l1.next
                l2 = l2.next
            point.next = new_point
            point = point.next
        if carry:
            new_point = ListNode(1)
            point.next = new_point
        return head.next

obj = Solution()
list1 = [1, 3, 4]
list2 = [4, 5, 6]
result = obj.addTwoNumbers(ListNode(list1), ListNode(list2))
print(result)