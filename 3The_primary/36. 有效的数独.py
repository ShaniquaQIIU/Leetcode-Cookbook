#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/22 09:42
# @Author  : Shaniqua Qiu
# @File    : 36. 有效的数独.py

from typing import List
from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 在第 i 个行中是否出现过
        # 在第 j 个列中是否出现过
        # 在第 j/3 + (i/3)*3个box中是否出现过
        lows, columns, boxes = defaultdict(set), defaultdict(set), defaultdict(set)
        for low in range(9):
            for col in range(9):
                if board[low][col].isdigit():  # 或者用 board[low][col] != '.'也可以
                    # 以下三个if判断是不是在行、列和 3*3宫格内存在有重复数字*
                    if board[low][col] in lows[low]:
                        return False
                    if board[low][col] in columns[col]:
                        return False
                    # 这里3*3宫格缩小1/3*
                    if board[low][col] in boxes[low // 3, col // 3]:
                        return False
                    # 没存在加入行、列和 3*3宫格*
                    lows[low].add(board[low][col])
                    columns[col].add(board[low][col])
                    boxes[low // 3, col // 3].add(board[low][col])

        return True


