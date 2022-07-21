#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/18 11:39
# @Author  : Shaniqua Qiu
# @File    : 53. 最大子序和.py

# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] = max(nums[i], nums[i-1] +  nums[i])
        return max(nums)
