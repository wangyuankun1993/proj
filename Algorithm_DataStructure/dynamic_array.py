# -*- coding:utf-8 -*-
# Product Name: PyCharm
# Project Name: proj
# File Name: dynamic_array.py
# Date: 2022/02/02 15:00:08
# Author: wangyuankun
# Function: This file is to achieve xxx function!
import ctypes

class DynamicArray():
    """A dynamic array class akin to a simplified Python list."""
    def __init__(self):
        """Create an empty array."""
        self._n = 0 # count actual elements
        self._capacity = 1 # default array capacity
        self._A = self._make_array(self._capacity) # lew-level array

    def __len__(self):
        """Return number of elements stored in the array."""
        return self._n

    def __getitem__(self, k):
        """Return element at index k."""
        if not 0 <= k < self._n:
            raise IndexError('invalid index')
        return self._A[k]

    def append(self, obj):
        """Add object to end of the array."""
        if self._n == self._capacity: # not enough room
            self._resize(2 * self._capacity) # so double capacity
        self._A[self._n] = obj
        self._n += 1

    def _resize(self, c): # nonpublic utity
        """Resize internal array to capacity c."""
        B = self._make_array(c) # now (bigger) array
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c

    def _make_array(self, c): # nonpublic utitity
        """Return new array with capacity c."""
        return (c * ctypes.py_object)() # see ctypes documentation
