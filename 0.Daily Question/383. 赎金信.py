#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/5 19:54
# @Author  : Shaniqua Qiu
# @File    : 383. 赎金信.py

# 为了不在赎金信中暴露字迹，从杂志上搜索各个需要的字母，组成单词来表达意思。
# 给你一个赎金信 (ransomNote) 字符串和一个杂志(magazine)字符串，判断 ransomNote 能不能由 magazines 里面的字符构成。
# 如果可以构成，返回 true ；否则返回 false 。
# magazine 中的每个字符只能在 ransomNote 中使用一次。

from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return (r:=Counter(ransomNote)) & Counter(magazine) == r


