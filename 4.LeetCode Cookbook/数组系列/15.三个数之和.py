#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/2 13:26
# @Author  : Shaniqua Qiu
# @File    : 15.三个数之和.py

# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？
# 请你找出所有满足条件且不重复的三元组。
# 注意：答案中不可以包含重复的三元组。

from typing import List

# 2020-12-02  双指针法
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        nums.sort()
        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i>0 and nums[i] == nums[i-1]:    # 跳过重复值
                continue
            left, right = i+1, len(nums)-1
            while (left < right):
                sum =  nums[left]+nums[right]+nums[i]
                if sum == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -=1
                    while left<right and nums[left] == nums[left-1]:
                        left += 1     # 跳过重复值
                    while left<right and nums[right] == nums[right+1]:
                        right -=1
                elif sum >0:
                    right -= 1
                else:
                    left += 1
        return res
