#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/30 19:46
# @Author  : Shaniqua Qiu
# @File    : 242. 有效的字母异位词.py

# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

import collections


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list_s = list(s)
        list_t = list(t)
        list_s.sort()
        list_t.sort()
        return list_s == list_t


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return collections.Counter(s) == collections.Counter(t)