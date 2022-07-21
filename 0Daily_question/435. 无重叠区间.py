#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/31 09:58
# @Author  : Shaniqua Qiu
# @File    : 435. 无重叠区间.py

# 给定一个区间的集合，找到需要移除区间的最小数量，使剩余区间互不重叠。
# 注意:
# 可以认为区间的终点总是大于它的起点。
# 区间 [1,2] 和 [2,3] 的边界相互“接触”，但没有相互重叠。

from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        intervals = sorted(intervals, key=lambda x: x[1])

        ans = 0
        end = -float('inf')  # 结束时间
        for i in intervals:
            if i[0] >= end:
                ans += 1
                end = i[1]
        return len(intervals) - ans
