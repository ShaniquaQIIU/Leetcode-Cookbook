#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/8/9 19:09
# @Author  : Shaniqua Qiu
# @File    : 1137. 第 N 个泰波那契数.py


# 泰波那契序列 Tn 定义如下： 
# T0 = 0, T1 = 1, T2 = 1, 且在 n >= 0 的条件下 Tn+3 = Tn + Tn+1 + Tn+2
# 给你整数 n，请返回第 n 个泰波那契数 Tn 的值。
# https://leetcode-cn.com/problems/n-th-tribonacci-number/


class Solution:
    def tribonacci(self, n: int) -> int:
        demo = {}
        def dp(n):
            if n in demo:
                return demo[n]
            if n == 0:
                return 0
            if n == 1:
                return 1
            if n == 2:
                return 1
            demo[n] = dp(n-1)+dp(n-2)+dp(n-3)
            return demo[n]
        return dp(n)
