#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/8 17:38
# @Author  : Shaniqua Qiu
# @File    : 200. 岛屿数量.py

# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
# 岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
# 此外，你可以假设该网格的四条边均被水包围。
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def inArea(grid, i, j):
            if i >=0 and i < len(grid) and j>=0 and j < len(grid[0]):
                return True
            return False

        def dfs(grid, i, j):
            if not inArea(grid, i, j): # 判断坐标点是否在网格内，越界返回
                return
            if grid[i][j] != '1': # 不是岛屿返回
                return
            grid[i][j] = '2'  # 数值2表示已经遍历的格子，防止重复遍历
            dfs(grid, i + 1, j)
            dfs(grid, i, j + 1)
            dfs(grid, i - 1, j)
            dfs(grid, i, j - 1)

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(grid, i, j)
                    count += 1
        return count
