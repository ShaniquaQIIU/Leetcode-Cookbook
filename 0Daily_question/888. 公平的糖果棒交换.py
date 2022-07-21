#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/3 15:13
# @Author  : Shaniqua Qiu
# @File    : 888. 公平的糖果棒交换.py


# 2021-02-01 0Daily_question
# 给定一个未经排序的整数数组，找到最长且 连续递增的子序列，并返回该序列的长度。
# 连续递增的子序列 可以由两个下标 l 和 r（l < r）确定，如果对于每个 l <= i < r，都有 nums[i] < nums[i + 1] ，
# 那么子序列 [nums[l], nums[l + 1], ..., nums[r - 1], nums[r]] 就是连续递增子序列。
from typing import List


class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        sum_A = sum(A)
        sum_B = sum(B)
        hashdict = {}
        for i in A:
            if i not in hashdict:
                hashdict[i] = 0           # 把其中的一个表存入字典
        for j in B:
            i = j + (sum_A - sum_B) // 2  # 无论是A多还是B多，直接用加法就解决
            if i in hashdict.keys():
                return [i , j]