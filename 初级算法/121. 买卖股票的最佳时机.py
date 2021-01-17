#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/17 12:16
# @Author  : Shaniqua Qiu
# @File    : 121. 买卖股票的最佳时机.py
from typing import List

# 前i天的最大收益 = max{前i-1天的最大收益，第i天的价格-前i-1天中的最小价格}
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_p, max_p = float('inf'), 0
        for i in range(len(prices)):
            max_p = max(max_p,  prices[i] - min_p)
            min_p = min(min_p,  prices[i])
        return max_p
