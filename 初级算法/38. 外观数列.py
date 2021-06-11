#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/7 14:49
# @Author  : Shaniqua Qiu
# @File    : 38. 外观数列.py

# 给定一个正整数 n ，输出外观数列的第 n 项。
# 「外观数列」是一个整数序列，从数字 1 开始，序列中的每一项都是对前一项的描述。
# 你可以将其视作是由递归公式定义的数字字符串序列：
# countAndSay(1) = "1"
# countAndSay(n) 是对 countAndSay(n-1) 的描述，然后转换成另一个数字字符串。


class Solution:
    def countAndSay(self, n: int) -> str:
        pre, cur = '', '1'
        # 从第 2 项开始
        for _ in range(1, n):
            pre, cur = cur, ''  # 当前项是下一项的前项
            start, end = 0, 0  # 指针
            while end < len(pre):
                while end < len(pre) and pre[start] == pre[end]:   # 记录重复元素次数
                    end += 1
                cur += str(end-start) + pre[start]
                start = end # 更新 start，开始记录下一个元素
        return cur

