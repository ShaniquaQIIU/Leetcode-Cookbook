#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5Study_plan/19 18:34
# @Author  : Shaniqua Qiu
# @File    : 168. Excel表列名称.py

# 给定一个正整数，返回它在 Excel 表中相对应的列名称。


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        if columnNumber < 0:
            return ''
        s = ''
        while columnNumber:
            mod = columnNumber%26
            if mod == 0:
                s+= 'Z'
                columnNumber = columnNumber //26 -1
            else:
                s += chr(columnNumber%26+64)
                columnNumber //= 26
        return s[::-1]