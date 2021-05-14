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

# 2021-05-14
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        left, rigth = 0, len(s)-1
        while left<=rigth:
            if not s[left].isalnum():
                left += 1
                continue  # 不用continue继续执行的话，多个连续的符号无法忽略
            if not s[rigth].isalnum():
                rigth -= 1
                continue
            if s[left] == s[rigth]:
                left += 1
                rigth -= 1
            else:
                return False
        return True