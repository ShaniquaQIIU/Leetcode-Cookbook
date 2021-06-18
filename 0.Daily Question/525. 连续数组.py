#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/3 09:54
# @Author  : Shaniqua Qiu
# @File    : 525. 连续数组.py

# 给定一个二进制数组 nums , 找到含有相同数量的 0 和 1 的最长连续子数组，并返回该子数组的长度。
from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        hashmap = {0:-1}
        cnt, res = 0, 0
        for i,num in enumerate(nums):
            if num:
                cnt += 1
            else:
                cnt -= 1
            if cnt in hashmap:
                res = max(res, i - hashmap[cnt])
            else:
                hashmap[cnt] = i
        return res
