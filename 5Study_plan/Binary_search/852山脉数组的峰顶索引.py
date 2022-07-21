#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/7/18 16:58
# @Author  : Shaniqua Qiu
# @File    : 852山脉数组的峰顶索引.py


# 符合下列属性的数组 arr 称为 山脉数组 ：
# arr.length >= 3
# 存在 i（0 < i < arr.length - 1）使得：
# arr[0] < arr[1] < ... arr[i-1] < arr[i]
# arr[i] > arr[i+1] > ... > arr[arr.length - 1]
# 给你由整数组成的山脉数组 arr ，返回任何满足 arr[0] < arr[1] < ... arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1] 的下标 i 。
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/peak-index-in-a-mountain-array

from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 0, len(arr)-1
        while left < right:
            mid = (right-left)//2 + left
            if arr[mid] < arr[mid+1]:
                left = mid+1
            else:
                right = mid
        return left
