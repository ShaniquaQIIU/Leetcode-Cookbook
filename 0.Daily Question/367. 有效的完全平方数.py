#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/4 09:57
# @Author  : Shaniqua Qiu
# @File    : 367. 有效的完全平方数.py

# https://leetcode-cn.com/problems/valid-perfect-square/
# 给定一个 正整数 num ，编写一个函数，如果 num 是一个完全平方数，则返回 true ，否则返回 false 。
# 进阶：不要 使用任何内置的库函数，如  sqrt 。

# 利用 1+3+5+7+9+…+(2n-1)=n^2，即完全平方数肯定是前n个连续奇数的和
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        x = 1
        while num > 0:
            num -= x
            x += 2
        return num == 0


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return num**0.5 % 1 == 0