#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5Study_plan/26 17:52
# @Author  : Shaniqua Qiu
# @File    : 169. 多数元素.py

# 给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。
# 你可以假设数组是非空的，并且给定的数组总是存在多数元素。
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]


# 摩尔投票法
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res, cnt = 0, 0
        for i in range(len(nums)):
            if not cnt:
                res = nums[i]
                cnt = 1
            else:
                cnt += 1 if res==nums[i] else -1
        return res
