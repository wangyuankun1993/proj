# -*- coding:utf-8 -*-
# Product Name: PyCharm
# Project Name: proj
# File Name: linked_deque.py
# Date: 2022/02/04 17:36:00
# Author: wangyuankun
# Function: This file is to achieve xxx function!
from doubly_linked_base import _DoublyLinkedBase
class LinkedDeque(_DoublyLinkedBase):
    """Double-ended queue implementation based on a doubly linked list."""
    def first(self):
        if self.is_empty():
            raise Empty('Deque is empty')
        return self._header._next._element

    def last(self):
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._tailer._prev._element

    def insert_first(self, e):
        self._insert_between(e, self._header, self._header._next)

    def insert_last(self, e):
        self._insert_between(e, self._tailer._prev, self._tailer)

    def delete_first(self):
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._delete_node(self._header._next)

    def delete_last(self):
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._delete_node(self._tailer._prev)
