#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/3 15:05
# @Author  : Shaniqua Qiu
# @File    : 724. 寻找数组的中心索引.py

# 2021-01-28 0Daily_question
# 给你一个整数数组nums，请编写一个能够返回数组 “中心索引” 的方法。
# 数组 中心索引 是数组的一个索引，其左侧所有元素相加的和等于右侧所有元素相加的和。
# 如果数组不存在中心索引，返回 -1 。如果数组有多个中心索引，应该返回最靠近左边的那一个。
# 注意：中心索引可能出现在数组的两端。

from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if not len(nums):
            return -1
        left, right = {0: 0}, {len(nums)-1: 0}
        for i in range(1, len(nums)):
            left[i] = left[i-1] + nums[i-1]  # 计算当前数左边数之和
        for j in range(len(nums)-2, -1, -1):
            right[j] = right[j+1] + nums[j+1]  # 计算当前数右边数之和
        for k in left.keys():
            if left[k] == right[k]:
                return k
        return -1