# -*- coding:utf-8 -*-
# Product Name: PyCharm
# Project Name: proj
# File Name: match_html.py
# Date: 2022/02/03 16:28:51
# Author: wangyuankun
# Function: This file is to achieve xxx function!
def is_matched_html(raw):
    """Return True if all HTML tags are properly match;False otherwise."""
    S = ArrayStack()
    j = raw.find('<') # find first '<' character
    while j != -1:
        k = raw.find('>', j+1) # find next '>' character
        if k == -1:
            return False
        tag = raw[j+1:k] # strip away < >
        if not tag.startswith('/'):
            S.push(tag)
        else:
            if S.is_empty():
                return False
            if tag[1:] != S.pop():
                return False # mismatched delimiter
        j = raw.find('<', k+1) # find next '<' character
    return S.is_empty()
