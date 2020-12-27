#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/27 10:45
# @Author  : Shaniqua Qiu
# @File    : 205. 同构字符串.py


# 给定两个字符串 s 和 t，判断它们是否是同构的。
# 如果 s 中的字符可以被替换得到 t ，那么这两个字符串是同构的。
# 所有出现的字符都必须用另一个字符替换，同时保留字符的顺序。两个字符不能映射到同一个字符上，但字符可以映射自己本身。


from typing import List


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return all(s.index(s[i]) == t.index(t[i])  for i in range(len(s)))