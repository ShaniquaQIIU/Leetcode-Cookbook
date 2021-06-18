#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/13 15:47
# @Author  : Shaniqua Qiu
# @File    : 448. 找到所有数组中消失的数字.py

# 给定一个范围在 1 ≤ a[i] ≤ n (n = 数组大小 ) 的 整型数组，数组中的元素一些出现了两次，另一些只出现一次。
# 找到所有在 [1, n] 范围之间没有出现在数组中的数字。
from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        return set([i for i in range(1, len(nums)+1)]) - set(nums)
