#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/7/21 15:02
# @Author  : Shaniqua Qiu
# @File    : 367有效的完全平方数.py

# https://leetcode-cn.com/problems/valid-perfect-square/
# 给定一个 正整数 num ，编写一个函数，如果 num 是一个完全平方数，则返回 true ，否则返回 false 。
# 进阶：不要 使用任何内置的库函数，如  sqrt 。

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num==1:
            return True
        left, right = 0, num
        while left <= right:
            mid = (left + right)//2
            if num/mid == mid:
                return True
            if num/mid > mid:
                left = mid+1
            else:
                right = mid-1
        return False
