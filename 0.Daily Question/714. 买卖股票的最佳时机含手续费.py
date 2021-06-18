#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/6 10:57
# @Author  : Shaniqua Qiu
# @File    : 714. 买卖股票的最佳时机含手续费.py

# 2020-12-17 题目
# 给定一个整数数组 prices，其中第 i 个元素代表了第 i 天的股票价格 ；非负整数 fee 代表了交易股票的手续费用。
# 你可以无限次地完成交易，但是你每笔交易都需要付手续费。如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。
# 返回获得利润的最大值。

from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        no_stock, has_stock = 0, -prices[0]
        for i in range(1, len(prices)):
            no_stock = max(no_stock, has_stock+prices[i]-fee)  # 考略当日是否卖出
            has_stock = max(has_stock, no_stock-prices[i])    # 考略当日是否买入
        return no_stock
