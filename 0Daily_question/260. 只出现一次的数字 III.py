#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/4 16:47
# @Author  : Shaniqua Qiu
# @File    : 260. 只出现一次的数字 III.py

# https://leetcode-cn.com/problems/single-number-iii/
# 给定一个整数数组 nums，其中恰好有两个元素只出现一次，其余所有元素均出现两次。
# 找出只出现一次的那两个元素。你可以按 任意顺序 返回答案。

from typing import List
from functools import reduce


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        d = reduce(lambda x,y:x^y,nums)
        d = d & -d
        a = b = 0
        for i in nums:
            # 根据这位1将所有num分成两组，两个不同的数会在两组，其他仍然是相同的
            if i & d:
                a ^= i
            else:
                b ^= i
        return [a,b]
