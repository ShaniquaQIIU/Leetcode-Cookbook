#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/3 09:44
# @Author  : Shaniqua Qiu
# @File    : 1446. 连续字符.py

# 给你一个字符串 s ，字符串的「能量」定义为：只包含一种字符的最长非空子字符串的长度。
# 请你返回字符串的能量。

class Solution:
    def maxPower(self, s: str) -> int:
        n = len(s)
        dp = [1] * n
        for i in range(1, n):
            if s[i] == s[i - 1]: dp[i] = dp[i - 1] + 1
        return max(dp)
