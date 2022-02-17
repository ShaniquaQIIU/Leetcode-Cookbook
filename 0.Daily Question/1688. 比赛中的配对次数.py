#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/1/26 09:39
# @Author  : Shaniqua Qiu
# @File    : 1688. 比赛中的配对次数.py

# https://leetcode-cn.com/problems/count-of-matches-in-tournament/
# 给你一个整数 n ，表示比赛中的队伍数。比赛遵循一种独特的赛制：
# 如果当前队伍数是 偶数 ，那么每支队伍都会与另一支队伍配对。总共进行 n / 2 场比赛，且产生 n / 2 支队伍进入下一轮。
# 如果当前队伍数为 奇数 ，那么将会随机轮空并晋级一支队伍，其余的队伍配对。总共进行 (n - 1) / 2 场比赛，且产生 (n - 1) / 2 + 1 支队伍进入下一轮。
# 返回在比赛中进行的配对次数，直到决出获胜队伍为止。


class Solution:
    def numberOfMatches(self, n: int) -> int:
        pairs = 0
        while n > 1:
            if n % 2 == 1:
                pairs += (n - 1) // 2
                n = (n - 1) // 2 + 1
            elif n % 2 == 0:
                pairs += n // 2
                n //= 2

        return pairs


class Solution:
    def numberOfMatches(self, n: int) -> int:
        return n-1
