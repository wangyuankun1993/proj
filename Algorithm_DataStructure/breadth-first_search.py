# -*- coding: utf-8 -*-
# Product Name: PyCharm
# Project Name: Algorithm_DataStructure
# File Name: breadth-first_search.py
# Date: 2022/06/12 14:04:55
# Author: wangyuankun
# Function: This file is to achieve breadth-first_search function.
from collections import deque

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

def breadth_first_search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = [] # 这个数组用于记录检查过的人
    while search_queue:
        person = search_queue.popleft()
        if not person in searched: # 仅当这个人没检查过时才检查
            if person_is_seller(person):
                print(person + " is a mango seller!")
                return True
            else:
                search_queue += graph[person]
                searched.append(person) # 将这个人标记为检查过
    return False

def person_is_seller(name):
    return name[-1] == 'm'

obj = breadth_first_search("you")