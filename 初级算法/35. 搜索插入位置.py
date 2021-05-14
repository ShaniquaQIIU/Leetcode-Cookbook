#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/13 18:45
# @Author  : Shaniqua Qiu
# @File    : 35. 搜索插入位置.py

# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        return len(nums)