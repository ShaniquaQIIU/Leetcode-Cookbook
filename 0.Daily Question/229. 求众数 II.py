#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/25 09:50
# @Author  : Shaniqua Qiu
# @File    : 229. 求众数 II.py

# 给定一个大小为 n 的整数数组，找出其中所有出现超过 ⌊ n/3 ⌋ 次的元素。
# https://leetcode-cn.com/problems/majority-element-ii/

from typing import List
from collections import Counter


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        return [n for n, v in Counter(nums).items() if v > len(nums) // 3]
