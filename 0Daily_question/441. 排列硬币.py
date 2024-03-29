#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/14 10:12
# @Author  : Shaniqua Qiu
# @File    : 441. 排列硬币.py

# https://leetcode-cn.com/problems/arranging-coins/
# 你总共有 n 枚硬币，并计划将它们按阶梯状排列。对于一个由 k 行组成的阶梯，其第 i 行必须正好有 i 枚硬币。阶梯的最后一行 可能 是不完整的。
# 给你一个数字 n ，计算并返回可形成 完整阶梯行 的总行数。

class Solution:
    def arrangeCoins(self, n: int) -> int:
        # i * (i+1) <= 2 * n
        l, r = 1, n
        n *= 2
        while l < r:
            mid = (l + r + 1) // 2
            s = mid * (mid + 1)
            if s == n:
                return mid
            elif s > n:
                r = mid - 1
            else:
                l = mid
        return l
