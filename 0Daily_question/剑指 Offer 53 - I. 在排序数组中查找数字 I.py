#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/16 14:10
# @Author  : Shaniqua Qiu
# @Site    : https://leetcode-cn.com/problems/zai-pai-xu-shu-zu-zhong-cha-zhao-shu-zi-lcof/
# @File    : 剑指 Offer 53 - I. 在排序数组中查找数字 I.py


# 统计一个数字在排序数组中出现的次数。
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left < right:
            mid = left + (right-left)//2
            if nums[mid] < target:
                left = mid+1
            else:
                right = mid
        count = 0
        while left< len(nums) and nums[left] == target:
            count += 1
            left += 1
        return count



class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return nums.count(target)
