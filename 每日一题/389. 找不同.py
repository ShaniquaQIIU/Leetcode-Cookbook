#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/18 09:48
# @Author  : Shaniqua Qiu
# @File    : 389. 找不同.py

# 给定两个字符串 s 和 t，它们只包含小写字母。
# 字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。
# 请找出在 t 中被添加的字母。

# 2020-12-18
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if len(s) == 0:
            return t
        list_s, list_t =  list(s), list(t)
        list_s.sort()
        list_t.sort()
        for i in range(len(list_s)):
            if ord(list_s[i]) ^ ord(list_t[i]) != 0:
                return list_t[i]
        return list_t[-1]


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return chr(sum(map(ord, t)) - sum(map(ord, s)))

