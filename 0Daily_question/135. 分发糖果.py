#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/24 14:16
# @Author  : Shaniqua Qiu
# @File    : 135. 分发糖果.py

# 规则定义： 设学生 AA 和学生 BB 左右相邻，AA 在 BB 左边；
# 左规则： 当 ratings_B>ratings_Aratings 时，BB 的糖比 AA 的糖数量多。
# 右规则： 当 ratings_A>ratings_Bratings 时，AA 的糖比 BB 的糖数量多。

from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        left = [1 for _ in range(len(ratings))]
        right = left[:]
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]: left[i] = left[i - 1] + 1
        count = left[-1]
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]: right[i] = right[i + 1] + 1
            count += max(left[i], right[i])
        return count
