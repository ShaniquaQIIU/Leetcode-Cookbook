#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/8/10 14:05
# @Author  : Shaniqua Qiu
# @File    : 413. 等差数列划分.py

# https://leetcode-cn.com/problems/arithmetic-slices/
# 如果一个数列 至少有三个元素 ，并且任意两个相邻元素之差相同，则称该数列为等差数列。
# 例如，[1,3,5,7,9]、[7,7,7,7] 和 [3,-1,-5,-9] 都是等差数列。
# 给你一个整数数组 nums ，返回数组 nums 中所有为等差数组的 子数组 个数。
# 子数组 是数组中的一个连续序列。

from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [0] * N
        for i in range(1, N-1):
            if nums[i-1] + nums[i+1] == nums[i] * 2:
                dp[i] = dp[i-1] + 1
        return sum(dp)
