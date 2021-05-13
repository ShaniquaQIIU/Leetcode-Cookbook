#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/6 10:26
# @Author  : Shaniqua Qiu
# @File    : 80. 删除有序数组中的重复项 II.py

# 给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使每个元素 最多出现两次 ，返回删除后数组的新长度。
# 不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = count = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                count += 1
            else:
                count = 1
            if count <= 2:
                nums[index] = nums[i]
                index += 1
        return index


class Solution:
    ''' 快慢指针'''
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 0
        for fast in range(len(nums)):
            if slow < 2 or nums[fast] != nums[slow - 2]:
                nums[slow] = nums[fast]
                slow += 1
        return slow
