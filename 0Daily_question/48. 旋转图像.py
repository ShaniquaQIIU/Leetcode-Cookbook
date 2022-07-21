#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/6 10:57
# @Author  : Shaniqua Qiu
# @File    : 48. 旋转图像.py

# 2020-12-19 题目
# 给定一个 n × n 的二维矩阵表示一个图像。
# 将图像顺时针旋转 90 度。
# 说明：你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。


from typing import List


class Solution:
    # TNT 第一反应还是需要辅助数组
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        matrix_new = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                matrix_new[j][n - i - 1] = matrix[i][j]
        matrix[:] = matrix_new


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n // 2):          # 水平翻转
            for j in range(n):
                matrix[i][j], matrix[n - i - 1][j] = matrix[n - i - 1][j], matrix[i][j]
        for i in range(n):               # 主对角线翻转
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


class Solution:
    # 评论总是最简洁的
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix[:] = zip(*matrix[::-1])   # 水平翻转，再压缩-同列聚合在一起=主对角线翻转
        # zip(*matrix)[::-1]  #逆时针旋转


