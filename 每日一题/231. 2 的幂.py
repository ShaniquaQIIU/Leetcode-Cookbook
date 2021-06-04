#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/31 10:39
# @Author  : Shaniqua Qiu
# @File    : 231. 2 的幂.py

# 给你一个整数 n，请你判断该整数是否是 2 的幂次方。如果是，返回 true ；否则，返回 false 。
# 如果存在一个整数 x 使得 n == 2x ，则认为 n 是 2 的幂次方。


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        if n == 1:
            return True
        if not n & (n-1): # 100 & 011
            return True
        return False