#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/21 16:38
# @Author  : Shaniqua Qiu
# @File    : 20. 有效的括号.py

# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
# 有效字符串需满足：
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。

class Solution:
    def isValid(self, s: str) -> bool:
        while '{}' in s or '()' in s or '[]'in s:
            s = s.replace('()', "")
            s = s.replace('[]', "")
            s = s.replace('{}', "")
        return len(s)==0

# 2021-10-15 stack
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        par_map = {')': '(', ']': '[', '}': '{'}
        for c in s:
            if c not in par_map:
                stack.append(c)
            elif not stack or par_map[c] != stack.pop():
                return False
        return not stack