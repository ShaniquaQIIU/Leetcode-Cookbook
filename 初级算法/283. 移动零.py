#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/22 09:34
# @Author  : Shaniqua Qiu
# @File    : 283. 移动零.py

# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
# 输入: [0,1,0,3,12]
# 输出: [1,3,12,0,0]


from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if nums is None: return
        j = 0
        while 0 in nums:
            nums.remove(0)
            j += 1
        for j in range(j):
            nums.append(0)
        return nums


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_count = 0
        for i in range(len(nums)):
            idx = i-zero_count
            if nums[idx] == 0:
                nums.pop(idx)
                nums.append(0)
                zero_count+=1
