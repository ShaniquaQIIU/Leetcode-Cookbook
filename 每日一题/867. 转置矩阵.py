#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/26 16:31
# @Author  : Shaniqua Qiu
# @File    : 867. 转置矩阵.py
from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        return [list(x) for x in zip(*matrix)]


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        res = []
        for i in range(n):
            x = []
            for j in range(m):
                x.append(matrix[j][i])
            res.append(x)
        return res