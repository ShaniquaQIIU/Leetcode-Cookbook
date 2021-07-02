#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/2 17:49
# @Author  : Shaniqua Qiu
# @Site    : https://leetcode-cn.com/problems/maximum-ice-cream-bars/
# @File    : 1833. 雪糕的最大数量.py

# 商店中新到 n 支雪糕，用长度为 n 的数组 costs 表示雪糕的定价，其中 costs[i] 表示第 i 支雪糕的现金价格。Tony 一共有 coins 现金可以用于消费，他想要买尽可能多的雪糕。
# 给你价格数组 costs 和现金量 coins ，请你计算并返回 Tony 用 coins 现金能够买到的雪糕的 最大数量 。
# 注意：Tony 可以按任意顺序购买雪糕。


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        cnt, res = 0, 0
        for i, cost in enumerate(costs):
            res += cost
            if res > coins:
                break
            cnt += 1
        return cnt

