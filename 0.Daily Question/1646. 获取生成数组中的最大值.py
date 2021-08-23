#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/8/23 14:07
# @Author  : Shaniqua Qiu
# @File    : 1646. 获取生成数组中的最大值.py

# 给你一个整数 n 。按下述规则生成一个长度为 n + 1 的数组 nums ：
# nums[0] = 0
# nums[1] = 1
# 当 2 <= 2 * i <= n 时，nums[2 * i] = nums[i]
# 当 2 <= 2 * i + 1 <= n 时，nums[2 * i + 1] = nums[i] + nums[i + 1]
# 返回生成数组 nums 中的 最大 值。


class Solution:
    def getMaximumGenerated(self, n: int) -> int:
    # 动态规划
        if n < 2:
            return n
        dp = [0]*(n+1)
        dp[1] = 1
        max_ = 1
        for i in range(2, n+1):
            if i % 2 == 0:
                dp[i] = dp[i//2]
            else:
                dp[i] = dp[i//2] + dp[i//2+1]
            max_ = max(max_, dp[i])
        return max_
