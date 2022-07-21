#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/26 10:23
# @Author  : Shaniqua Qiu
# @Site    : https://leetcode-cn.com/problems/check-if-all-the-integers-in-a-range-are-covered/
# @File    : 1893. 检查是否区域内所有整数都被覆盖.py

from typing import List
from collections import defaultdict


class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        diff = defaultdict(int)
        for l, r in ranges:
            diff[l] += 1
            diff[r+1] -= 1
        curr = 0
        for i in range(1, right + 1):
            curr += diff[i]
            if curr <= 0 and left <= i:
                return False
        return True
