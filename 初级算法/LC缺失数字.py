#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/22 17:12
# @Author  : Shaniqua Qiu
# @File    : LC缺失数字.py

# 给定一个包含 [0, n] 中 n 个数的数组 nums ，找出 [0, n] 这个范围内没有出现在数组中的那个数。
from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = (len(nums)+1)*len(nums)/2 - sum(nums)
        return int(n)

# 异或
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        for k, v in enumerate(nums):
            n ^= k ^ v
        return int(n)