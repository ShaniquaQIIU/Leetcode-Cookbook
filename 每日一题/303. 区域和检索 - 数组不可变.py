#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/1 17:08
# @Author  : Shaniqua Qiu
# @File    : 303. 区域和检索 - 数组不可变.py

# 给定一个整数数组 nums，求出数组从索引i到j（i≤j）范围内元素的总和，包含i、j两点。
# 实现 NumArray 类：
# NumArray(int[] nums) 使用数组 nums 初始化对象
# int sumRange(int i, int j) 返回数组 nums 从索引i到j（i≤j）范围内元素的总和，
#    包含i、j两点（也就是 sum(nums[i], nums[i + 1], ... , nums[j])）
from typing import List


class NumArray:
    def __init__(self, nums: List[int]):
        N = len(nums)
        self.preSum = [0] * (N + 1)
        for i in range(N):
            self.preSum[i + 1] = self.preSum[i] + nums[i]

    def sumRange(self, i: int, j: int) -> int:  # j - (i-1)
        return self.preSum[j + 1] - self.preSum[i]
