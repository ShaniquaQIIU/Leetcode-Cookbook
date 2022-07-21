#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5Study_plan/26 15:44
# @Author  : Shaniqua Qiu
# @File    : 172. 阶乘后的零.py

# 给定一个整数 n，返回 n! 结果尾数中零的数量。

class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        while n>=5:
            count += n//5
            n //= 5
        return count

