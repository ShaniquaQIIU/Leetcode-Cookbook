#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/18 17:21
# @Author  : Shaniqua Qiu
# @File    : 13. 罗马数字转整数.py


class Solution:
    def romanToInt(self, s: str) -> int:
        dict_roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        res = 0
        for i in range(len(s)):
            if i < len(s)-1 and dict_roman[s[i]] < dict_roman[s[i+1]] :
                res -= dict_roman[s[i]]
            else:
                res += dict_roman[s[i]]
        return res
