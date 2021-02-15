#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/15 15:40
# @Author  : Shaniqua Qiu
# @File    : 485. 最大连续1的个数.py

# 给定一个二进制数组， 计算其中最大连续1的个数。
# 注意：
# 输入的数组只包含 0 和1。
# 输入数组的长度是正整数，且不超过 10,000。
from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res, count = 0, 0
        for i, v in enumerate(nums):
            if v:
                count +=1
            else:
                res = max(count, res)
                count = 0
        return max(count, res)


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        substr = ''.join([str(i) for i in nums]).split('0')
        return len(max(substr))

