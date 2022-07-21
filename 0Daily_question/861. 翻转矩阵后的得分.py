#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/7 14:04
# @Author  : Shaniqua Qiu
# @File    : 861. 翻转矩阵后的得分.py

# 有一个二维矩阵A 其中每个元素的值为0或1。
# 移动是指选择任一行或列，并转换该行或列中的每一个值：将所有 0 都更改为 1，将所有 1 都更改为 0。
# 在做出任意次数的移动后，将该矩阵的每一行都按照二进制数来解释，矩阵的得分就是这些数字的总和。
# 返回尽可能高的分数。

from typing import List
from math import pow


class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        # 获取行、列值
        row, col = len(A), len(A[0])
        res = 0

        # 首列值全1
        for i in range(row):
            if A[i][0] == 0:
                A[i] = [0 if A[i][j] == 1 else 1 for j in range(col)]
        res += pow(2, col - 1) * row

        for j in range(1, col):
            count = 0
            for i in range(row):
                if A[i][j] == 1:  # 统计1的个数
                    count += 1
            count = max(count, row - count)  # 剩余列1的个数多于0的个数
            res += pow(2, col - j - 1) * count
        return int(res)


# 评论看到的算法，没有悟透 TNT
class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        n, m = len(A), len(A[0])
        res = n
        for i in range(1, m):
            res <<= 1
            s = sum([A[j][i] ^ A[j][0] for j in range(n)])
            res += max(s, n - s)
        return res