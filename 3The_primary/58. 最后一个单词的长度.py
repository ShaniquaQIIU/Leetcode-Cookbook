#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5Study_plan/13 18:53
# @Author  : Shaniqua Qiu
# @File    : 58. 最后一个单词的长度.py

# 给你一个字符串 s，由若干单词组成，单词之间用空格隔开。返回字符串中最后一个单词的长度。如果不存在最后一个单词，请返回 0 。


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        x = s.split(' ')
        for i in x[::-1]:
            if i != '':
                return len(i)
                break
        return 0


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        x = s.split()
        if not x:
            return 0
        return len(x[-1])