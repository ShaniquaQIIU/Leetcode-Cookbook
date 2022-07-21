#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/21 09:42
# @Author  : Shaniqua Qiu
# @File    : 746. 使用最小花费爬楼梯.py

# 数组的每个索引作为一个阶梯，第 i个阶梯对应着一个非负数的体力花费值 cost[i](索引从0开始)。
# 每当你爬上一个阶梯你都要花费对应的体力花费值，然后你可以选择继续爬一个阶梯或者爬两个阶梯。
# 您需要找到达到楼层顶部的最低花费。在开始时，你可以选择从索引为 0 或 1 的元素作为初始阶梯。

from typing import List


# 2020-12-21 万物皆可动态规划
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cur, prev = 0, 0
        for i in range(2, len(cost)+1):
            prev, cur = cur, min(cur+cost[i-1], prev+cost[i-2])
        return cur

