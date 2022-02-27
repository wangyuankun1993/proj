# -*- coding:utf-8 -*-
# Product Name: PyCharm
# Project Name: proj
# File Name: circular_queue.py
# Date: 2022/02/04 15:31:29
# Author: wangyuankun
# Function: This file is to achieve xxx function!
class CircularQueue():
    """Queue implementation using circularly linked list for storage."""
    class _Node():
        """Lightweight, nonpublic class for storing a singly linked node."""
        (ormitted here;indentical to that of LinkedStack._Node)

    def __init__(self):
        """Create an empty queue."""
        self._tail = None
        self._size = 0

    def __len__(self):
        """Return the number of elements in the queue."""
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        head = self._tail._next
        return head._element

    def dequeue(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        oldhead = self._tail._next
        if self._size == 1:
            self._tail = None
        else:
            self._tail._next = oldhead._next
        self._size -= 1
        return oldhead._element

    def enqueue(self, e):
        newest = self._Node(e, None)
        if self.is_empty():
            newest._next = newest
        else:
            newest._next = self._tail._next
            self._tail._next = newest
        self._tail = newest
        self._size += 1

    def rotate(self):
        if self._size > 0:
            self._tail = self._tail._next
