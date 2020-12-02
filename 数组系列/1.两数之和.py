#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/2 09:52
# @Author  : Shaniqua Qiu
# @File    : 1.两数之和.py

# 题目大意
# 在数组中找到 2 个数之和等于给定值的数字，结果返回 2 个数字在数组中的下标。

from typing import List

# 2020-06-15 暴力解法
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        value = 0
        for i in range(len(nums)):
            copy_list = nums.copy()
            copy_list.pop(i)
            value = target - nums[i]
            if value in copy_list:
                j = copy_list.index(value)
                j = j if (i>j) else j+1
                return [i, j]
        return None


# 2020-12-01  key、value
# 将list中的位置、值用键值对的方式存入字典
# 判断差值是否在字典中，即两数和等于目标值
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for k, v in enumerate(nums):
            num = target - v
            if num in hashmap:
                return [hashmap[num], k]
            hashmap[v] = k
        return None