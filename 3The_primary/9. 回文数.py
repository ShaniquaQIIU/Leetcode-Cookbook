#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5Study_plan/13 15:31
# @Author  : Shaniqua Qiu
# @File    : 9. 回文数.py

# 给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。
# 回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。例如，121 是回文，而 123 不是。

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        res, tmp = 0, x
        while tmp !=0:
            res = res*10 + tmp%10
            tmp //=10
        return True if res==x else False


class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]


import math


class Solution:
    # 翻转一半,  x//10==res - 位数为奇数时的判断
    def isPalindrome(self, x: int) -> bool:
        if x<0 or (x!=0 and x%10==0):
            return False
        elif x ==0:
            return True
        length = int(math.log(x, 10)) + 1
        res = 0
        for i in range(length//2):
            res = res*10+x%10
            x //= 10
        return True if x==res or x//10==res else False