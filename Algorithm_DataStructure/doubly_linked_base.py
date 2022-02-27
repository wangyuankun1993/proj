# -*- coding:utf-8 -*-
# Product Name: PyCharm
# Project Name: proj
# File Name: doubly_linked_base.py
# Date: 2022/02/04 16:45:10
# Author: wangyuankun
# Function: This file is to achieve xxx function!
class _DoublyLinkedBase():
    """A base class providing a doubly linked list representation."""
    class _Node:
        """Lightweight, nonpublic class for storing a doubly linked node."""
        (omitted here;see previous code fragment)

    def __init__(self):
        """Create an empty list."""
        self._header = self._Node(None, None, None)
        self.tailer = self._Node(None, None, None)
        self.header._next = self.tailer
        self.tailer._prev = self._header
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        newest = self._Node(e, predecessor, successor)
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest

    def _delete_node(self, node):
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element
        node._prev = node._next = node._element = None
        return element
