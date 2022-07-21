#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/9/7 18:37
# @Author  : Shaniqua Qiu
# @File    : 1221. 分割平衡字符串.py

# 在一个 平衡字符串 中，'L' 和 'R' 字符的数量是相同的。
# 给你一个平衡字符串 s，请你将它分割成尽可能多的平衡字符串。
# 注意：分割得到的每个字符串都必须是平衡字符串。
# 返回可以通过分割得到的平衡字符串的 最大数量 。


class Solution:
    def balancedStringSplit(self, s: str) -> int:
        n = len(s)
        res, cntL, cntR  = 0, 0, 0
        for r in range(n):
            c = s[r]
            if c == 'L':
                cntL += 1
            elif c == 'R':
                cntR += 1
            if cntL == cntR:
                res += 1
                cntL = 0
                cntR = 0
        return res