#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/18 09:24
# @Author  : Shaniqua Qiu
# @File    : 476. 数字的补数.py

# https://leetcode-cn.com/problems/number-complement/
# 给你一个 正整数 num ，输出它的补数。补数是对该数的二进制表示取反。

# 异或
class Solution:
    def findComplement(self, num: int) -> int:
        return num ^ (2**(len(bin(num))-2)-1)


# 字符串0/1取反
class Solution:
    def findComplement(self, num: int) -> int:
        bin_num = bin(num)[2:]
        bin_ans = map(lambda x: '0' if x == '1' else '1', bin_num)
        return int(''.join(bin_ans), 2)
