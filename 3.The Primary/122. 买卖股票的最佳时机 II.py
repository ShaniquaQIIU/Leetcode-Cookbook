#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/3 13:36
# @Author  : Shaniqua Qiu
# @File    : 122. 买卖股票的最佳时机 II.py

# 给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
# 设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。
# 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 贪心算法；不限制买入卖出次数，考虑当天收益为正即可卖出
        maxprofit = 0
        for i in range(1, len(prices)):
            if prices[i] - prices[i-1] >0:
                maxprofit += prices[i] - prices[i-1]
        return maxprofit


# 20210519 优化下，少一次计算
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(1, len(prices)):
            tmp = prices[i] - prices[i-1]
            if tmp > 0:
                max_profit += tmp
        return max_profit


# 动态规划
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        n = len(prices)
        dp = [[0]*2 for __ in range(n)]
        # dp[i][0] 表示当天不持有，dp[i][1] 表示当天持有
        dp[0][0] , dp[0][1] = 0, -prices[0]
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0]-prices[i])
        return dp[n-1][0]