#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/21 10:28
# @Author  : Shaniqua Qiu
# @File    : 171. Excel表列序号.py


# 给定一个Excel表格中的列名称，返回其相应的列序号。


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        for i in columnTitle:
            res *= 26
            res += ord(i) - ord('A') +1
        return res
