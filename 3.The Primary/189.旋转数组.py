#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/5 18:27
# @Author  : Shaniqua Qiu
# @File    : 189.旋转数组.py

# 给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
from typing import List


# python 切片
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        if len(nums) == 1 or len(nums) == 0 or k == 0:
            return
        nums[:-k], nums[-k:] = nums[-k:], nums[:-k]


# 2021-07-24
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n    # k的值可能比数组长度大，因此需要取余
        nums[:]= nums[k+1:]+nums[:-k]
