#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/31 11:57
# @Author  : Shaniqua Qiu
# @File    : 28. 实现 strStr().py

# 给定一个haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。
# 如果不存在，则返回 -1。

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == '':
            return 0

        return haystack.find(needle)    # 使用index找不到会报错

