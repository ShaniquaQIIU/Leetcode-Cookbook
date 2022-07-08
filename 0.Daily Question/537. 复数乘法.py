#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/2/25 14:12
# @Author  : Shaniqua Qiu
# @File    : 537. 复数乘法.py

# 复数 可以用字符串表示，遵循 "实部+虚部i" 的形式，并满足下述条件：
# 实部 是一个整数，取值范围是 [-100, 100]
# 虚部 也是一个整数，取值范围是 [-100, 100]
# i2 == -1
# 给你两个字符串表示的复数 num1 和 num2 ，请你遵循复数表示形式，返回表示它们乘积的字符串。
# 链接：https://leetcode-cn.com/problems/complex-number-multiplication


class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        # (a+bi)(c+di)=( ac-bd)+(bc+ad)i
        arr1 =  num1.split("+")
        arr2 =  num2.split("+")
        a, b = int(arr1[0]), int(arr1[1][:-1])
        c, d = int(arr2[0]), int(arr2[1][:-1])
        return str(a*c-b*d) + "+" + str(b*c+a*d) + "i"


