#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/9 15:33
# @Author  : Shaniqua Qiu
# @File    : 503. 下一个更大元素 II.py

# 给定一个循环数组（最后一个元素的下一个元素是数组的第一个元素），输出每个元素的下一个更大元素。
# 数字 x 的下一个更大的元素是按数组遍历顺序，这个数字之后的第一个比它更大的数，这意味着你应该循环地搜索它的下一个更大的数。如果不存在，则输出 -1。
from typing import List

# 用单调栈求解，此处栈内记录的是 nums 元素的下标
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        lens = len(nums)
        res = [ -1 for _ in range(lens)]
        stack = list()

        doubel_nums = nums + nums
        for k, v in enumerate(doubel_nums):
            while stack and nums[stack[-1]] < v:
                res[stack[-1]] = v
                stack.pop()
            if k < lens:
                stack.append(k)
        return res
