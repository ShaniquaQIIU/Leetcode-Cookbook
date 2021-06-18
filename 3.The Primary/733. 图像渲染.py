#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/15 17:19
# @Author  : Shaniqua Qiu
# @File    : 733. 图像渲染.py

# 有一幅以二维整数数组表示的图画，每一个整数表示该图画的像素值大小，数值在 0 到 65535 之间。
# 给你一个坐标 (sr, sc) 表示图像渲染开始的像素值（行 ，列）和一个新的颜色值 newColor，让你重新上色这幅图像。
# 为了完成上色工作，从初始坐标开始，记录初始坐标的上下左右四个方向上像素值与初始坐标相同的相连像素点，接着再记录这四个方向上符合条件的像素点与他们对应四个方向上像素值与初始坐标相同的相连像素点，……，重复该过程。将所有有记录的像素点的颜色值改为新的颜色值。
# 最后返回经过上色渲染后的图像。

from typing import List


# 同200.岛屿问题
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        def dfs(image, sr, sc, initColor, newColor):
            row, col = len(image), len(image[0])
            if not (0<=sr<row and 0<=sc<col): # 坐标越界
                return
            if image[sr][sc] == newColor or image[sr][sc] != initColor:
                return
            image[sr][sc] = newColor
            dfs(image, sr-1, sc, initColor, newColor)
            dfs(image, sr, sc-1, initColor, newColor)
            dfs(image, sr+1, sc, initColor, newColor)
            dfs(image, sr, sc+1, initColor, newColor)

        initColor = image[sr][sc]
        if initColor == newColor:
            return image
        dfs(image, sr, sc, initColor, newColor)
        return image