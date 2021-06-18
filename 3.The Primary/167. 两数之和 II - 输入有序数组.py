#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/19 18:04
# @Author  : Shaniqua Qiu
# @File    : 167. 两数之和 II - 输入有序数组.py

# 给定一个已按照 升序排列  的整数数组 numbers ，请你从数组中找出两个数满足相加之和等于目标数 target 。
# 函数应该以长度为 2 的整数数组的形式返回这两个数的下标值。numbers 的下标 从 1 开始计数 ，所以答案数组应当满足 1 <= answer[0] < answer[1] <= numbers.length 。
# 你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        left , right = 0, n-1
        while left < right:
            if numbers[right] == target - numbers[left]:
                return [left+1, right+1]
            elif numbers[right] > target - numbers[left]:
                right -= 1
            else:
                left +=1
        return None