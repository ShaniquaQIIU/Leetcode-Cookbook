#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/13 15:52
# @Author  : Shaniqua Qiu
# @File    : 119. 杨辉三角 II.py

# 2021-02-12 0.Daily Question
# 给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。
from typing import List


class Solution:  # 注意此题是从第0行开始的
    def getRow(self, rowIndex: int) -> List[int]:
        curr_row = []
        next_row = [1]
        for i in range(rowIndex):
            curr_row = next_row
            next_row = [0] * (len(curr_row) + 1)
            for j in range(len(next_row)):
                if j == 0 or j == len(next_row) - 1:
                    next_row[j] = 1
                else:
                    next_row[j] = curr_row[j-1] + curr_row[j]
        return next_row
