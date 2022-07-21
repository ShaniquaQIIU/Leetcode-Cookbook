#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/16 14:40
# @Author  : Shaniqua Qiu
# @File    : 561. 数组拆分 I.py

# 给定长度为2n的整数数组 nums ，你的任务是将这些数分成n 对,
# 例如 (a1, b1), (a2, b2), ..., (an, bn) ，使得从 1 到n 的 min(ai, bi) 总和最大。
# 返回该 最大总和 。
from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])
