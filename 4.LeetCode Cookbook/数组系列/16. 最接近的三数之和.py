#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/3 13:39
# @Author  : Shaniqua Qiu
# @File    : 16. 最接近的三数之和.py

# 给定一个包括n个整数的数组nums和 一个目标值target。
# 找出nums中的三个整数，使得它们的和与target最接近。
# 返回这三个数的和。假定每组输入只存在唯一答案。

from typing import List

# 双指针法
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums_len = len(nums)
        nums.sort()
        ans_sum = nums[0] + nums[1] + nums[2]
        for i in range(nums_len):
            left, right = i + 1, nums_len - 1
            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]
                if abs(curr_sum - target) < abs(ans_sum - target):
                    ans_sum = curr_sum
                if curr_sum > target:
                    right -= 1
                elif curr_sum < target:
                    left += 1
                else:
                    return target
        return ans_sum

