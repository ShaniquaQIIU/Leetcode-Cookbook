#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/14 10:09
# @Author  : Shaniqua Qiu
# @File    : 67. 二进制求和.py

# 给你两个二进制字符串，返回它们的和（用二进制表示）。
# 输入为 非空 字符串且只包含数字 1 和 0。


class Solution:
    '''
    class int(x, base=10)
    bin(20) '0b10100'
    '''
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a,2)+int(b,2))[2:]