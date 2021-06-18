#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/25 09:33
# @Author  : Shaniqua Qiu
# @File    : 455. 分发饼干.py

# 对每个孩子 i，都有一个胃口值g[i]，这是能让孩子们满足胃口的饼干的最小尺寸；并且每块饼干 j，都有一个尺寸 s[j]
# 如果 s[j]>= g[i]，我们可以将这个饼干 j 分配给孩子 i ，这个孩子会得到满足。
# 你的目标是尽可能满足越多数量的孩子，并输出这个最大数值。

# 2020-12-25 昨天发完糖果，今天来发饼干。贪心算法
from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        g_len, s_len = len(g), len(s)
        g_left = s_left = num_bist = 0
        while g_left < g_len and s_left < s_len:
            if g[g_left] <= s[s_left]:
                num_bist+=1
                g_left+=1
                s_left+=1
            else:
                s_left+=1
        return num_bist



