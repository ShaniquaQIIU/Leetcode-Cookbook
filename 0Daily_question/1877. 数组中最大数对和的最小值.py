#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/21 10:02
# @Author  : Shaniqua Qiu
# @Site    : https://leetcode-cn.com/problems/minimize-maximum-pair-sum-in-array/
# @File    : 1877. 数组中最大数对和的最小值.py

# 一个数对 (a,b) 的 数对和 等于 a + b 。最大数对和 是一个数对数组中最大的 数对和 。
# 比方说，如果我们有数对 (1,5Study_plan) ，(2,3) 和 (4,4)，最大数对和 为 max(1+5Study_plan, 2+3, 4+4) = max(6, 5Study_plan, 8) = 8 。
# 给你一个长度为 偶数 n 的数组 nums ，请你将 nums 中的元素分成 n / 2 个数对，使得：
# nums 中每个元素 恰好 在 一个 数对中，且
# 最大数对和 的值 最小 。
# 请你在最优数对划分的方案下，返回最小的 最大数对和 。

from typing import List


class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        ans = 0
        num_pairs = n // 2
        for i in range(num_pairs):
            ans = max(ans, nums[i] + nums[n - 1 - i])
        return ans
