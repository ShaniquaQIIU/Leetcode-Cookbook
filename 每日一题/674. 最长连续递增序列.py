#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/3 14:50
# @Author  : Shaniqua Qiu
# @File    : 674. 最长连续递增序列.py

# 2021-01-24 每日一题
# 给定一个未经排序的整数数组，找到最长且 连续递增的子序列，并返回该序列的长度。
# 连续递增的子序列 可以由两个下标 l 和 r（l < r）确定，如果对于每个 l <= i < r，都有 nums[i] < nums[i + 1] ，
# 那么子序列 [nums[l], nums[l + 1], ..., nums[r - 1], nums[r]] 就是连续递增子序列。
from typing import List


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        res = []
        i = 0
        while i < len(nums):
            num = 1
            while i < len(nums) - 1 and nums[i] < nums[i + 1]:
                num += 1
                i += 1

            if num > 0:
                res.append(num)
            i += 1

        return max(res) if res else 0

