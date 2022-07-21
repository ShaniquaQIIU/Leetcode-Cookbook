#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/22 14:37
# @Author  : Shaniqua Qiu
# @File    : 989. 数组形式的整数加法.py

# 输入：A = [1,2,0,0], K = 34
# 输出：[1,2,3,4]
# 解释：1200 + 34 = 1234
from typing import List


class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        s = ""
        for it in A:
            s += str(it)
        s = str(int(s) + K)
        return list(s)
