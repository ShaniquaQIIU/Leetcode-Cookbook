#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/1 22:34
# @Author  : Shaniqua Qiu
# @File    : 34. 在排序数组中查找元素的第一个和最后一个位置.py

# 2020-12-01 题目
# 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
# 如果数组中不存在目标值 target，返回 [-1, -1]。

from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if nums is None:
            return [-1,-1]
        if target not in nums:
            return [-1,-1]
        res = []
        for k, v in enumerate(nums):
            if v == target:
                res.append(k)
        return [res[0], res[-1]]
