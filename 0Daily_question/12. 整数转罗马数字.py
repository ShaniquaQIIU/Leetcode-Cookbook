#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5Study_plan/14 11:27
# @Author  : Shaniqua Qiu
# @File    : 12. 整数转罗马数字.py


class Solution:
    def intToRoman(self, num: int) -> str:
        list_int = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        list_roman = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
        res = ""
        for i in range(len(list_int)):
            while num >= list_int[i]:
                res += list_roman[i]
                num -= list_int[i]
        return res
