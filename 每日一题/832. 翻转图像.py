#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/26 16:02
# @Author  : Shaniqua Qiu
# @File    : 832. 翻转图像.py

# 给定一个二进制矩阵A，我们想先水平翻转图像，然后反转图像并返回结果。
# 水平翻转图片就是将图片的每一行都进行翻转，即逆序。例如，水平翻转[1, 1, 0]的结果是[0, 1, 1]。
# 反转图片的意思是图片中的0全部被1替换，1全部被0替换。例如，反转[0, 1, 1]的结果是[1, 0, 0]。
from typing import List
import math

class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        return [list(map(lambda x:1-x,row[::-1])) for row in A]


# 交换
class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for i in range(len(A)):
            for j in range(math.ceil(len(A[0])/2)):
                [A[i][j], A[i][-1-j]] = [1-A[i][-1-j], 1-A[i][j]]
        return A