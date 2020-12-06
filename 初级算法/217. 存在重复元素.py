#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/6 21:07
# @Author  : Shaniqua Qiu
# @File    : 217. 存在重复元素

# 给定一个整数数组，判断是否存在重复元素。
# 如果任意一值在数组中出现至少两次，函数返回 true 。如果数组中每个元素都不相同，则返回 false 。
from typing import List


class Solution:
    # 内置函数set去重
    def containsDuplicate(self, nums: List[int]) -> bool:
        set_nums = set(nums)
        if len(set_nums) < len(nums):
            return True
        else:
            return False


class Solution:
    # key value
    def containsDuplicate(self, nums: List[int]) -> bool:
        dic = {}
        for i in nums:
            if dic.get(i):
                return True
            dic[i] = 1
        return False