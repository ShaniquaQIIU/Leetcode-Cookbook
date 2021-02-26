#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/22 15:40
# @Author  : Shaniqua Qiu
# @File    : 766. 托普利茨矩阵.py

# 给你一个 m x n 的矩阵 matrix 。如果这个矩阵是托普利茨矩阵，返回 true ；否则，返回 false 。
# 如果矩阵上每一条由左上到右下的对角线上的元素都相同，那么这个矩阵是 托普利茨矩阵 。
from typing import List


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for i in range(len(matrix) - 1):
            if matrix[i][:-1] != matrix[i + 1][1:]:
                return False
        return True
