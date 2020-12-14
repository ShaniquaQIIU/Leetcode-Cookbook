#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/15 06:33
# @Author  : Shaniqua Qiu
# @File    : 738. 单调递增的数字.py

# 2020-12-15
# 给定一个非负整数 N，找出小于或等于 N 的最大的整数，同时这个整数需要满足其各个位数上的数字是单调递增
# 从前往后找到第一个不符合要求的位数，然后该位减一，后面的都变成9，再从头判断，执行整个过程，直到满足要求

class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        nums = list(str(N))
        i = 0
        index = len(nums)
        for i in range(len(nums)-1, 0, -1):
            if nums[i] < nums[i-1]:
                nums[i-1] = str(int(nums[i-1])-1)
                nums[i:] = ['9'] * (index - i)
        return int(''.join(nums))
