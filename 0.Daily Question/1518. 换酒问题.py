#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/12/17 14:42
# @Author  : Shaniqua Qiu
# @File    : 1518. 换酒问题.py

# 小区便利店正在促销，用 numExchange 个空酒瓶可以兑换一瓶新酒。你购入了 numBottles 瓶酒。
# 如果喝掉了酒瓶中的酒，那么酒瓶就会变成空的。
# 请你计算 最多 能喝到多少瓶酒。

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = numBottles

        cur = numBottles  # 空瓶数
        while cur >= numExchange:
            a, b = divmod(cur, numExchange)
            res += a
            cur = a + b
        return res
