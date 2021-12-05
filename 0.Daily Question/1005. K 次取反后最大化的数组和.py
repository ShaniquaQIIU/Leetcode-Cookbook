#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/5 19:59
# @Author  : Shaniqua Qiu
# @File    : 1005. K 次取反后最大化的数组和.py

# 给你一个整数数组 nums 和一个整数 k ，按以下方法修改该数组：
# 选择某个下标 i 并将 nums[i] 替换为 -nums[i] 。
# 重复这个过程恰好 k 次。可以多次选择同一个下标 i 。
# 以这种方式修改数组后，返回数组 可能的最大和 。

from typing import List
import heapq

class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        while k and nums:
            if nums[0] < 0:
                heapq.heappush(nums, -heapq.heappop(nums))
                k -= 1
            else:
                if nums[0] and k % 2:
                    heapq.heappush(nums, -heapq.heappop(nums))
                break
        return sum(nums)