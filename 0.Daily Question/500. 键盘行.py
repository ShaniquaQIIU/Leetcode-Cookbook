#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/4 16:21
# @Author  : Shaniqua Qiu
# @File    : 500. 键盘行.py

# https://leetcode-cn.com/problems/keyboard-row/

# 给你一个字符串数组 words ，只返回可以使用在 美式键盘 同一行的字母打印出来的单词。键盘如下图所示。
# 美式键盘 中：
# 第一行由字符 "qwertyuiop" 组成。
# 第二行由字符 "asdfghjkl" 组成。
# 第三行由字符 "zxcvbnm" 组成。

from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        d1,d2,d3 = set("qwertyuiop"),set("asdfghjkl"),set("zxcvbnm")
        ans = []
        for i in words:
            ri = i
            i = set(i.lower())
            # 判断当前字符串是否为一行，i & d == i
            if i & d1 == i or i & d2 == i or i & d3 == i:
                ans.append(ri)
        return ans
