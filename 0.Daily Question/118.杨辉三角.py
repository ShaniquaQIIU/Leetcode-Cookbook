#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/6 10:57
# @Author  : Shaniqua Qiu
# @File    : 118.杨辉三角.py

# 2020-12-06 题目
# 给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。

from typing import List
import math


class Solution:
    # 按定义解，在杨辉三角中，每个数是它左上方和右上方的数的和。
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(numRows):
            now = [1] * (i+1)
            if i>= 2:
                for j in range(1,i):
                    now[j] = pre[j-1] + pre[j]
            res.append(now)
            pre = now
        return res


class Solution:
    # 评论区看到一行代码
    # math.comb(n, k) 返回：一个整数值，表示从n个项目中选择k个项目(无重复且无顺序)的方式数量。
    def generate(self, numRows: int) -> List[List[int]]:
        return [[math.comb(i, j) for j in range(i + 1)] for i in range(numRows)]