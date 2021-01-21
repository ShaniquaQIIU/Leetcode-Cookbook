#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/21 14:35
# @Author  : Shaniqua Qiu
# @File    : 190. 颠倒二进制位.py

# 颠倒给定的 32 位无符号整数的二进制位。
class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(0, 32):
            res += (1&(n>>i))<<(31-i)
        return res