#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/31 10:31
# @Author  : Shaniqua Qiu
# @File    : 342. 4的幂.py

# 给定一个整数，写一个函数来判断它是否是 4 的幂次方。如果是，返回 true ；否则，返回 false 。
# 整数 n 是 4 的幂次方需满足：存在整数 x 使得 n == 4x


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        x = 4
        while x>0 and x < n:
            x <<= 2
        return n == 1 or n == x
