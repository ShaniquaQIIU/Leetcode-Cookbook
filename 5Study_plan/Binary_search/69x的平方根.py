#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/7/22 17:05
# @Author  : Shaniqua Qiu
# @File    : 69x的平方根.py

# 给你一个非负整数 x ，计算并返回 x 的 算术平方根 。
# 由于返回类型是整数，结果只保留 整数部分 ，小数部分将被 舍去 。
# 注意：不允许使用任何内置指数函数和算符，例如 pow(x, 0.5) 或者 x ** 0.5 。
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/sqrtx


class Solution:
    def mySqrt(self, x: int) -> int:
        left, right, ans = 0, x, None
        while left <= right:
            mid = (left+right)//2
            if mid * mid <= x:
                ans = mid
                left = mid+1
            else:
                right = mid-1
        return ans

