#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/5Study_plan 10:16
# @Author  : Shaniqua Qiu
# @File    : 830. 较大分组的位置.py

# 所有包含大于或等于三个连续字符的分组为 较大分组 。
from typing import List

class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        # i, j为相同字母的开始索引, 结束索引的下一个
        r, i, j = [], 0, 0
        while j < len(s):
            # 如果字母相同, j自增
            if s[j] == s[i]:
                j += 1
                continue
            # 索引差超过3
            if j - i >= 3:
                r.append([i, j - 1])
            i = j
        # 终止条件: 相同字母在末尾
        if j - i >= 3:
            r.append([i, j - 1])
        return r