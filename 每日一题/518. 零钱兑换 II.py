#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/10 13:44
# @Author  : Shaniqua Qiu
# @File    : 518. 零钱兑换 II.py

# 给定不同面额的硬币和一个总金额。写出函数来计算可以凑成总金额的硬币组合数。假设每一种面额的硬币有无限个。
from typing import List


# 类似题目：爬楼梯
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0 for __ in range(amount+1)]
        dp[0] = 1
        for i in coins:
            for j in range(amount+1):
                if j>=i:
                    dp[j] += dp[j-i]
        return dp[amount]
