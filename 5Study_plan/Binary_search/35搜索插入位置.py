#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/7/18 16:33
# @Author  : Shaniqua Qiu
# @File    : 35搜索插入位置.py


# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
# 请必须使用时间复杂度为 O(log n) 的算法。
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/search-insert-position

from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (right-left)//2 + left
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid+1
            else:
                right = mid-1
        return left


