#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/14 10:21
# @Author  : Shaniqua Qiu
# @File    : 414. 第三大的数.py

# https://leetcode-cn.com/problems/third-maximum-number/
# 给你一个非空数组，返回此数组中 第三大的数 。如果不存在，则返回数组中最大的数。

from typing import List
import heapq

K = 3


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        pq = []
        for num in set(nums):
            heapq.heappush(pq, num)
            if len(pq) > K:
                heapq.heappop(pq)
        return heapq.heappop(pq) if len(pq) == K else pq[-1]