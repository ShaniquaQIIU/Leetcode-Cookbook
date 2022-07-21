#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/7/18 15:50
# @Author  : Shaniqua Qiu
# @File    : 704二分查找.py

# 给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/binary-search

from typing import List


# 2022-07-18
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (right-left)//2 + left
            num = nums[mid]
            if num == target:
                return mid
            elif num < target:
                left +=1
            else:
                right -=1
        return -1


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (right-left)//2 + left
            num = nums[mid]
            if num == target:
                return mid
            elif num < target:
                left = mid+1
            else:
                right = mid-1
        return -1