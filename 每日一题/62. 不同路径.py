#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/9 09:35
# @Author  : Shaniqua Qiu
# @File    : 62. 不同路径.py

# 2020-12-09 这是道数学题目
# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
# 问总共有多少条不同的路径？

import math


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return math.comb(m+n-2, m-1)
