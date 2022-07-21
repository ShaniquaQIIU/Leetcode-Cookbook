#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/23 13:48
# @Author  : Shaniqua Qiu
# @File    : 387. 字符串中的第一个唯一字符.py

# 给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。
from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        list_s = list(s)
        count_s = Counter(list_s)
        for k, v in count_s.items():
            if v == 1:
                return s.index(k)
        return -1
