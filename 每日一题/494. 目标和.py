#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/7 09:43
# @Author  : Shaniqua Qiu
# @File    : 494. 目标和.py

# 给你一个整数数组 nums 和一个整数 target 。
# 向数组中的每个整数前添加 '+' 或 '-' ，然后串联起所有整数，可以构造一个 表达式 ：
# 例如，nums = [2, 1] ，可以在 2 之前添加 '+' ，在 1 之前添加 '-' ，然后串联起来得到表达式 "+2-1" 。
# 返回可以通过上述方法构造的、运算结果等于 target 的不同 表达式 的数目。
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        tot_sum = sum(nums)
        if tot_sum < target:
            return 0
        positive_sum = (tot_sum + target) // 2
        if (tot_sum + target) % 2 == 1:
            return 0

        dp = [0 for _ in range(positive_sum + 1)]
        dp[0] = 1
        for num in nums:
            for x in range(positive_sum, num - 1, -1):
                dp[x] += dp[x - num]
        return dp[positive_sum]

# 2021-06-08 dfs 会遇到超时问题
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        def dfs(nums, S, i, cur):
            if i == len(nums):
                return 1 if cur == S else 0
            left = dfs(nums, S, i + 1, cur + nums[i])
            right = dfs(nums, S, i + 1, cur - nums[i])
            return left + right

        return dfs(nums, S, 0, 0)
