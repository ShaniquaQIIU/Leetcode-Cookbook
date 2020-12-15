#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/6 10:57
# @Author  : Shaniqua Qiu
# @File    : 290. 单词规律.py

# 2020-12-16 题目
# 给定一种规律 pattern 和一个字符串 str ，判断 str 是否遵循相同的规律。
# 这里的 遵循 指完全匹配，例如， pattern 里的每个字母和字符串 str 中的每个非空单词之间存在着双向连接的对应规律。。

from typing import List


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        t = s.split()
        if len(pattern) != len(t):  # 长度不一致
            return False
        dct = {}
        for i in range(len(pattern)):
            if pattern[i] not in dct:
                if t[i] in dct.values():
                    return False
                dct[pattern[i]] = t[i]    # 存值 {"a": "dog"}
            else:
                if dct[pattern[i]] != t[i]:
                    return False
        return True


# 别人的方法总是很简便
# map() 会根据提供的函数对指定序列做映射。
# 第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表。
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        t = s.split()
        return list(map(pattern.index, pattern))==list(map(t.index,t))


# python 3.8 支持，海象运算   tmp := s.split()
# https://docs.python.org/3/whatsnew/3.8.html#assignment-expressions
# zip: {('b', 'cat'), ('c', 'cat'), ('a', 'dog')}
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        tmp = s.split()
        return False if len(tmp) != len(pattern) else len(set(zip(pattern, tmp))) == len(set(tmp)) == len(set(pattern))