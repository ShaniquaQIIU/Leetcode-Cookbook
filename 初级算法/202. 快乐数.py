#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/4 17:13
# @Author  : Shaniqua Qiu
# @File    : 202. 快乐数.py

# 编写一个算法来判断一个数 n 是不是快乐数。
# 「快乐数」定义为：
# 对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和。
# 然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。
# 如果 可以变为  1，那么这个数就是快乐数。
# 如果 n 是快乐数就返回 true ；不是，则返回 false 。


class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True

        def tosquare(num):
            res = 0
            while num:
                res += (num % 10) ** 2
                num //= 10
            return res

        while True:
            n = tosquare(n)
            if n < 10:
                if n == 1 or n == 7:
                    return True
                return False



