#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/12 10:33
# @Author  : Shaniqua Qiu
# @File    : 228. 汇总区间.py

# 给定一个无重复元素的有序整数数组 nums 。
# 返回 恰好覆盖数组中所有数字 的 最小有序 区间范围列表。
# 也就是说，nums 的每个元素都恰好被某个区间范围所覆盖，并且不存在属于某个范围但不属于 nums 的数字 x 。
from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = 0
        res = []
        while n < len(nums):
            if n+1 < len(nums) and nums[n]+1 == nums[n+1]:
                m = n
                while n+1 < len(nums) and nums[n]+1 == nums[n+1]:
                    n += 1
                res.append("{}->{}".format(nums[m], nums[n]))
            else:
                res.append(str(nums[n]))
            n +=1
        return res

