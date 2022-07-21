#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5Study_plan/14 11:36
# @Author  : Shaniqua Qiu
# @File    : 69. x 的平方根.py

# 实现 int sqrt(int x) 函数。
# 计算并返回 x 的平方根，其中 x 是非负整数。
# 由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。


class Solution:   # 超时
    def mySqrt(self, x: int) -> int:
        left, right, mid = 1, x, 1+(x-1)//2
        while left <= right:
            mid = left+(right-left)//2
            if mid == x/mid:
                return mid
            elif mid > x/mid:
                right -= 1
            else:
                left += 1
        return right


class Solution:  # 牛顿迭代
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        right = x
        while right > x / right:
            right = (right + x / right) // 2

        return int(right)