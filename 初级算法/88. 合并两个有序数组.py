#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/15 17:13
# @Author  : Shaniqua Qiu
# @File    : 88. 合并两个有序数组.py
from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:] = nums2[:n]
        nums1.sort()