#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/18 16:49
# @Author  : Shaniqua Qiu
# @File    : 412. Fizz Buzz.py

# 写一个程序，输出从 1 到 n 数字的字符串表示。
# 如果n是3的倍数，输出“Fizz”；
# 如果n是5的倍数，输出“Buzz”；
# 如果n同时是3和5的倍数，输出 “FizzBuzz”。

from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for i in range(1, n+1):
            if i%15 == 0 :
                res.append("FizzBuzz")
            elif i%3 == 0 :
                res.append("Fizz")
            elif i%5 == 0 :
                res.append("Buzz")
            else:
                res.append(str(i))
        return res