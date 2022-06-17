# -*- coding: utf-8 -*-
# Product Name: PyCharm
# Project Name: json
# File Name: jsonValueFind.py
# Date: 2022/04/03 22:56:45
# Author: wangyuankun
# Function: This file is to achieve jsonToDict function.
import json
def json_value_find(json_data):

    # Judge function
    def judge_func(node_data):
        if isinstance(node_data, dict):
            key_value_iter = (x for x in node_data.items())
        elif isinstance(node_data, list):
            key_value_iter = (x for x in enumerate(node_data))
        else:
            return 0

        for key, value in key_value_iter:
            result = {}
            if isinstance(value, (dict, list)):
                yield from judge_func(value)
                result[key] = value
                print(result)
            else:
                yield key, value
                result[key] = value
                print(result)

    dict_data = json.loads(json_data)
    return list(judge_func(dict_data))

json_data = """{"name": "wangyuankun", "age": "18", "height": "170", "ID": "123456",
             "colors": [
                 {"color1": "red"},
                 {"color2": "black"},
                 {"color3": "blue"}
             ],
             "class": [
                 {"class1": "Chinese"},
                 {"class2": "English"},
                 {"class3": "France"}
             ]
             }"""
obj = json_value_find(json_data)
