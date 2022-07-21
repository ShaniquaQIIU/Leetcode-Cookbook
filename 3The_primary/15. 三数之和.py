#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/17 16:49
# @Author  : Shaniqua Qiu
# @File    : 15. 三数之和.py

# https://leetcode-cn.com/problems/3sum/
# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。
# 注意：答案中不可以包含重复的三元组。
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        nums.sort()
        res = []
        for k, v in enumerate(nums[:-2]):
            if k >=1 and v == nums[k-1]:
                continue
            d = {}
            for x in nums[k+1:]:
                if x not in d:
                    d[-v-x] = 0
                elif d[x] == 0:
                    res.append((v,-v-x,x))
                    d[x] += 1
        return res


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        nums.sort()
        res = []
        for i in range(len(nums)-2):
            if i >=1 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[i]+nums[l]+nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    res.append((nums[i],nums[l],nums[r]))
                    while l<r and nums[l]==nums[l+1]:
                        l+=1
                    while l<r and nums[r]==nums[r-1]:
                        r-=1
                    l+=1
                    r-=1
        return res

