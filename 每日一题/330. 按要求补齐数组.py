#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/29 13:49
# @Author  : Shaniqua Qiu
# @File    : 330. 按要求补齐数组.py

# 给定一个已排序的正整数数组 nums，和一个正整数n 。
# 从[1, n]区间内选取任意个数字补充到nums中，使得[1, n]区间内的任何数字都可以用nums中某几个数字的和来表示。
# 请输出满足上述要求的最少需要补充的数字个数。
from typing import List


class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        add, i, count = 1, 0, 0
        while add <= n:
            if i < len(nums) and nums[i] <= add:
                add += nums[i] # from [1, add] to [1, add + nums[i]]
                i += 1
            else:
                add += add # from [1, add] to [1, 2add]
                count += 1
        return count

