#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/15 16:51
# @Author  : Shaniqua Qiu
# @File    : 542. 01 矩阵.py

# 给定一个由 0 和 1 组成的矩阵，找出每个元素到最近的 0 的距离。
# 两个相邻元素间的距离为 1 。
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        if not mat or not mat[0]:
            return mat
        locs, row, col = [], len(mat), len(mat[0])
        ans = [[-1] * col for _ in range(row)]
        for i in range(row):
            for j in range(col):
                if not mat[i][j]:  # 坐标0到0的距离为0
                    locs.append((i, j))
                    ans[i][j] = 0

        step = 0
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while locs:
            step += 1
            tmp = []
            for i, j in locs:  # 更新每个点周围的4个点
                for dx, dy in dirs:
                    x, y = i + dx, j + dy
                    if 0 <= x < row and 0 <= y < col and ans[x][y] < 0:  # 新探索的有效点
                        ans[x][y] = step
                        tmp.append((x, y))
            locs = tmp
        return ans
