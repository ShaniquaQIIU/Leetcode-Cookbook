#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/1 10:31
# @Author  : Shaniqua Qiu
# @File    : 605. 种花问题.py

# 假设有一个很长的花坛，一部分地块种植了花，另一部分却没有。可是，花不能种植在相邻的地块上，它们会争夺水源，两者都会死去。
# 给你一个整数数组flowerbed 表示花坛，由若干 0 和 1 组成，其中 0 表示没种植花，1 表示种植了花。
# 另有一个数n ，能否在不打破种植规则的情况下种入n朵花？能则返回 true ，不能则返回 false。

from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # 当flowerbed[i-1] == flowerbed[i] == flowerbed[i+1] == 0时，
        # 我们可以在i处种下一朵花
        if not n:
            return True
        length = len(flowerbed)
        for i in range(length-1):   #i为当前位置
            if flowerbed[i]:
                continue
            if not flowerbed[i] and not flowerbed[i+1]:
                if i == 0:  # 开始边界
                    flowerbed[i] = 1
                    n -= 1
                if i > 0 and not flowerbed[i-1]:
                    flowerbed[i] = 1
                    n -= 1
        if not flowerbed[length-1] and not flowerbed[length-2]:   # 结束边界
            n -= 1
        return True if n <= 0 else False

