#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/13 14:17
# @Author  : Shaniqua Qiu
# @Site    : https://leetcode-cn.com/problems/sort-characters-by-frequency/
# @File    : 451. 根据字符出现频率排序.py


# 给定一个字符串，请将字符串里的字符按照出现的频率降序排列。


class Solution:
    def frequencySort(self, s: str) -> str:
        d = {}
        for i in s:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        t=sorted(d.items(), key = lambda i:i[1],reverse=True)
        res = ""
        for i in t:
            n = i[1]
            while n:
                res += i[0]
                n -= 1
        return res

