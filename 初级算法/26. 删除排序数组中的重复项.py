#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/2 13:42
# @Author  : Shaniqua Qiu
# @File    : 26. 删除排序数组中的重复项.py

# 给定一个排序数组，你需要在 原地 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
# 不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        length = 0
        for index in range(1, len(nums)):   #遍历数组
            if nums[index] != nums[length]:
                length += 1
                nums[length] = nums[index]
        return length+1

