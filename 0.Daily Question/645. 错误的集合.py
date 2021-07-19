#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/13 14:19
# @Author  : Shaniqua Qiu
# @Site    : https://leetcode-cn.com/problems/set-mismatch/
# @File    : 645. 错误的集合.py

# 集合 s 包含从 1 到 n 的整数。不幸的是，因为数据错误，导致集合里面某一个数字复制了成了集合里面的另外一个数字的值，导致集合 丢失了一个数字 并且 有一个数字重复 。
# 给定一个数组 nums 代表了集合 S 发生错误后的结果。
# 请你找出重复出现的整数，再找到丢失的整数，将它们以数组的形式返回。

from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        a, b, n = sum(set(nums)), sum(nums), len(nums)
        return [b-a, n*(n+1)//2-a]
