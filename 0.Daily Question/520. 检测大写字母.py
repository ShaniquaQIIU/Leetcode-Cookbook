#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/13 09:53
# @Author  : Shaniqua Qiu
# @File    : 520. 检测大写字母.py

# https://leetcode-cn.com/problems/detect-capital/
# 我们定义，在以下情况时，单词的大写用法是正确的：
# 全部字母都是大写，比如 "USA" 。
# 单词中所有字母都不是大写，比如 "leetcode" 。
# 如果单词不只含有一个字母，只有首字母大写， 比如 "Google" 。
# 给你一个字符串 word 。如果大写用法正确，返回 true ；否则，返回 false 。


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word.islower() or word.isupper() or word.istitle()



