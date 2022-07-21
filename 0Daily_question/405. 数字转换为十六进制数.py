#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/14 10:32
# @Author  : Shaniqua Qiu
# @File    : 405. 数字转换为十六进制数.py

# https://leetcode-cn.com/problems/convert-a-number-to-hexadecimal/
# 给定一个整数，编写一个算法将这个数转换为十六进制数。对于负整数，我们通常使用 补码运算 方法。
# 注意:
# 十六进制中所有字母(a-f)都必须是小写。
# 十六进制字符串中不能包含多余的前导零。如果要转化的数为0，那么以单个字符'0'来表示；对于其他情况，十六进制字符串中的第一个字符将不会是0字符。 
# 给定的数确保在32位有符号整数范围内。
# 不能使用任何由库提供的将数字直接转换或格式化为十六进制的方法。

CONV = "0123456789abcdef"


class Solution:
    def toHex(self, num: int) -> str:
        ans = []
        # 32位2进制数，转换成16进制 -> 4个一组，一共八组
        for _ in range(8):
            ans.append(num%16)
            num //= 16
            if not num:
                break
        return "".join(CONV[n] for n in ans[::-1])