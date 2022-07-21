#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/4 15:47
# @Author  : Shaniqua Qiu
# @File    : 14. 最长公共前缀.py

# 编写一个函数来查找字符串数组中的最长公共前缀。
# 如果不存在公共前缀，返回空字符串 ""。

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        min_str = min(strs)
        max_str = max(strs)
        # print(min_str, max_str)
        for i in range(len(min_str)):
            if  min_str[i] != max_str[i]:
                return min_str[:i]
        return min_str