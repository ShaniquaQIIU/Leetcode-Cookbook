#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/20 17:22
# @Author  : Shaniqua Qiu
# @File    : 191. 位1的个数.py

# 编写一个函数，输入是一个无符号整数（以二进制串的形式），返回其二进制表达式中数字位数为 '1' 的个数（也被称为汉明重量）。
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n :
            n &= (n-1)
            res += 1
        return res
