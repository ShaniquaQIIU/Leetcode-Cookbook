#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/8/9 19:18
# @Author  : Shaniqua Qiu
# @File    : 611. 有效三角形的个数.py

# https://leetcode-cn.com/problems/valid-triangle-number/
# 给定一个包含非负整数的数组，你的任务是统计其中可以组成三角形三条边的三元组个数。

from typing import List
import bisect   # https://docs.python.org/zh-cn/3/library/bisect.html 数组二分查找算法


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        ans = 0
        for i in range(n - 2):
            for j in range(i+1, n - 1):
                idx = bisect.bisect_left(nums, nums[i] + nums[j])
                if idx > j:
                    ans += idx - 1 - j
        return ans
