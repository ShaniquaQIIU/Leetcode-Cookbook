#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/20 17:26
# @Author  : Shaniqua Qiu
# @File    : 461. 汉明距离.py

# 两个整数之间的汉明距离指的是这两个数字对应二进制位不同的位置的数目。
# 给出两个整数 x 和 y，计算它们之间的汉明距离。

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count('1')