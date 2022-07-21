#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/8/25 19:22
# @Author  : Shaniqua Qiu
# @File    : 787. K 站中转内最便宜的航班.py

# 有 n 个城市通过一些航班连接。给你一个数组 flights ，
# 其中 flights[i] = [fromi, toi, pricei] ，表示该航班都从城市 fromi 开始，以价格 pricei 抵达 toi。
# 现在给定所有的城市和航班，以及出发城市 src 和目的地 dst，
# 你的任务是找到出一条最多经过 k 站中转的路线，使得从 src 到 dst 的 价格最便宜 ，并返回该价格。
# 如果不存在这样的路线，则输出 -1。

from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # dp[i][d] 记录经过k次转机后到达d城市的最小花费
        dp = [[float('inf')]*n for i in range(k+1)]
        # 初始化0次转机直达的花费
        for s, d, p in flights:
            if s == src :
                dp[0][d] = p
        for i in range(1, k+1):
            for s, d, p in flights:
                # 状态转移，第k次转机到达d城市的最小花费 = min (第k-1次转机到达d城市的最小花费,第k-1次转机到达s城市的最小花费 +s到达d的花费p,第k次转机到达d城市的最小花费)
                dp[i][d] = min(dp[i-1][d], dp[i-1][s]+p, dp[i][d])
        return dp[-1][dst] if dp[-1][dst] != float('inf') else -1


