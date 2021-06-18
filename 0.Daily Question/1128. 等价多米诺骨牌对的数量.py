#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/3 14:59
# @Author  : Shaniqua Qiu
# @File    : 1128. 等价多米诺骨牌对的数量.py

# 2021-01-27 0.Daily Question
# 给你一个由一些多米诺骨牌组成的列表dominoes。
# 如果其中某一张多米诺骨牌可以通过旋转 0度或 180 度得到另一张多米诺骨牌，我们就认为这两张牌是等价的。
# 形式上，dominoes[i] = [a, b]和dominoes[j] = [c, d]等价的前提是a==c且b==d，或是a==d 且b==c。
# 在 0<= i < j < dominoes.length的前提下，找出满足dominoes[i] 和dominoes[j]等价的骨牌对 (i, j) 的数量。

from typing import List


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        ans = 0
        d = dict()
        for d1, d2 in dominoes:
            # 排序后加入字典
            index = tuple(sorted((d1, d2)))
            if index in d:
                d[index] += 1
            else:
                d[index] = 1
        # 计算答案，排列组合的结果
        for i in d:
            ans += d[i] * (d[i] - 1) // 2
        return ans