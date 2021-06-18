#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/19 18:57
# @Author  : Shaniqua Qiu
# @File    : 316. 去除重复字母.py

# 2020-12-20 题目
# 给你一个字符串 s ，请你去除字符串中重复的字母，使得每个字母只出现一次。需保证 返回结果的字典序最小（要求不能打乱其他字符的相对位置）。

import collections


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        letter_counter = collections.Counter(s)
        remian_letter = []

        for c in s:
            if c not in remian_letter:
                while remian_letter and c < remian_letter[-1] and  letter_counter[remian_letter[-1]] > 0:
                    remian_letter.pop()
                remian_letter.append(c)
            letter_counter[c] -= 1
        return ''.join(remian_letter)