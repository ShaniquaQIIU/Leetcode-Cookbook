#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/1 11:39
# @Author  : Shaniqua Qiu
# @File    : 896. 单调数列.py

# 如果数组是单调递增或单调递减的，那么它是单调的。
# 如果对于所有 i <= j，A[i] <= A[j]，那么数组 A 是单调递增的。 如果对于所有 i <= j，A[i]> = A[j]，那么数组 A 是单调递减的。
# 当给定的数组 A是单调数组时返回 true，否则返回 false。
from typing import List


class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        ins_flag, des_flag = 0, 0
        for i in range(len(A)-1):
            if A[i] < A[i+1]:
                ins_flag = 1
            elif A[i] > A[i+1]:
                des_flag = 1
        return False if ins_flag + des_flag == 2 else True