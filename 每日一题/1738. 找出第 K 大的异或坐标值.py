#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/19 17:22
# @Author  : Shaniqua Qiu
# @File    : 1738. 找出第 K 大的异或坐标值.py

# 给你一个二维矩阵 matrix 和一个整数 k ，矩阵大小为 m x n 由非负整数组成。
# 矩阵中坐标 (a, b) 的 值 可由对所有满足 0 <= i <= a < m 且 0 <= j <= b < n 的元素 matrix[i][j]（下标从 0 开始计数）执行异或运算得到。
# 请你找出 matrix 的所有坐标中第 k 大的值（k 的值从 1 开始计数）。

from typing import List


class Solution:
    # 横向扫描后再纵向扫描
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(1,n):
                matrix[i][j] ^= matrix[i][j-1]

        for j in range(n):
            for i in range(1,m):
                matrix[i][j] ^= matrix[i-1][j];
        ans = []
        for i in range(m):
            for j in range(n):
                ans.append(matrix[i][j])
        ans.sort()
        return ans[len(ans) - k]