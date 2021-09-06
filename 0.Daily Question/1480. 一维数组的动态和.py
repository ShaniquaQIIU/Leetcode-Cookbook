#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/8/28 09:11
# @Author  : Shaniqua Qiu
# @File    : 1480. 一维数组的动态和.py

# 给你一个数组 nums 。数组「动态和」的计算公式为：runningSum[i] = sum(nums[0]…nums[i]) 。
# 请返回 nums 的动态和。

from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        return nums
