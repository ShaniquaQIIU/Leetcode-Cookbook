#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/18 16:36
# @Author  : Shaniqua Qiu
# @File    : 198. 打家劫舍.py

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) < 2:
            return nums[0]
        dp = {0:nums[0], 1: max(nums[0],nums[1])}
        for i in range(2, len(nums)):
            dp[i] = max(nums[i]+dp[i-2], dp[i-1])
        # print(dp)
        return max(dp.values())