#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/31 10:40
# @Author  : Shaniqua Qiu
# @File    : 125. 验证回文串.py

# 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(filter(str.isalnum, s)).lower()
        return s == s[::-1]
