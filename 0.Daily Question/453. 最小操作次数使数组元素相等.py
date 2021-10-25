#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/20 10:19
# @Author  : Shaniqua Qiu
# @File    : 453. 最小操作次数使数组元素相等.py

# https://leetcode-cn.com/problems/minimum-moves-to-equal-array-elements/
# 给你一个长度为 n 的整数数组，每次操作将会使 n - 1 个元素增加 1 。返回让数组所有元素相等的最小操作次数。

from typing import List


class Solution:
    def minMoves(self, nums: List[int]) -> int:
        target = min(nums)
        return sum(num-target for num in nums)


class Solution:
    def minMoves(self, nums: List[int]) -> int:
        return sum(nums) - min(nums) * len(nums)
