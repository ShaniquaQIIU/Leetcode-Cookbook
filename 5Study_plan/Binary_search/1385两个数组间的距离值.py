#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/7/21 15:45
# @Author  : Shaniqua Qiu
# @File    : 1385两个数组间的距离值.py

# 给你两个整数数组 arr1 ， arr2 和一个整数 d ，请你返回两个数组之间的 距离值 。
# 「距离值」 定义为符合此距离要求的元素数目：对于元素 arr1[i] ，不存在任何元素 arr2[j] 满足 |arr1[i]-arr2[j]| <= d 。
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/find-the-distance-value-between-two-arrays

from typing import List


class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        cnt = 0
        for x in arr1:
            if all(abs(x-y) > d for y in arr2):
                cnt += 1
        return cnt


class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        cnt = len(arr1)
        for i in range(len(arr1)):
            left, right = 0, len(arr2)-1
            while left <= right:
                mid = (left + right)//2
                if abs(arr2[mid] - arr1[i]) <= d:
                    cnt -= 1
                    break
                else:
                    if arr1[i] - arr2[mid] < 0:
                        right = mid - 1
                    else:
                        left = mid + 1
        return cnt