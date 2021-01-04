#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/4 11:47
# @Author  : Shaniqua Qiu
# @File    : 509. 斐波那契数.py

# F(0) = 0，F(1) = 1
# F(n) = F(n - 1) + F(n - 2)，其中 n > 1

class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        return self.fib(n-1) + self.fib(n-2)


class Solution:
    def fib(self, n: int) -> int:
        cur, nxt = 0, 1
        for i in range(n):
            cur, nxt = nxt, cur+nxt
        return cur