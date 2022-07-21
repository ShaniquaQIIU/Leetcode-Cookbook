#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/8 16:30
# @Author  : Shaniqua Qiu
# @File    : 150. 逆波兰表达式求值.py

# 根据 逆波兰表示法，求表达式的值。
# 有效的算符包括 +、-、*、/ 。每个运算对象可以是整数，也可以是另一个逆波兰表达式。
# 说明：
# 整数除法只保留整数部分。
# 给定逆波兰表达式总是有效的。换句话说，表达式总会得出有效数值且不存在除数为 0 的情况。

from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = []
        for i in tokens:
            if i == "+":
                res.append(res.pop()+res.pop())
            elif i == "-":
                res.append(-res.pop()+res.pop())
            elif i == "*":
                res.append(res.pop()*res.pop())
            elif i == "/":
                res.append(int(1/res.pop()*res.pop()))
            else:
                res.append(int(i))
        return res.pop()