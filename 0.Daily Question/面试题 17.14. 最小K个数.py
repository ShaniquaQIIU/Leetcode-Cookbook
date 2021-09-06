#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/9/6 19:22
# @Author  : Shaniqua Qiu
# @File    : 面试题 17.14. 最小K个数.py


# 设计一个算法，找出数组中最小的k个数。以任意顺序返回这k个数均可。
from typing import List
import heapq


class Solution1:
    def smallestK(self, arr: List[int], k: int) -> List[int]:
        return sorted(arr)[:k]


class Solution:
    def smallestK(self, arr: List[int], k: int) -> List[int]:
        heapq.heapify(arr)
        res = []
        for i in range(k):
            res.append(heapq.heappop(arr))
        return res