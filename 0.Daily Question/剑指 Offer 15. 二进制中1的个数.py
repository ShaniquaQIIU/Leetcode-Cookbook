#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/24 17:03
# @Author  : Shaniqua Qiu
# @Site    : https://leetcode-cn.com/problems/er-jin-zhi-zhong-1de-ge-shu-lcof/
# @File    : 剑指 Offer 15. 二进制中1的个数.py

# 请实现一个函数，输入一个整数（以二进制串形式），输出该数二进制表示中 1 的个数。例如，把 9 表示成二进制是 1001，有 2 位是 1。因此，如果输入 9，则该函数输出 2。


class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += 1
            n &= n - 1
        return res