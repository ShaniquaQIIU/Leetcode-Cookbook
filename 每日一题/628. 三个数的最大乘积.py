#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/20 09:48
# @Author  : Shaniqua Qiu
# @File    : 628. 三个数的最大乘积.py

# 给定一个整型数组，在数组中找出由三个数组成的最大乘积，并输出这个乘积。
from typing import List


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        # 负负得正
        return max(nums[-1] * nums[-2] *nums[-3], nums[-1] * nums[0] *nums[1])