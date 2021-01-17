#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/17 11:28
# @Author  : Shaniqua Qiu
# @File    : 1232. 缀点成线.py

# 在一个XY 坐标系中有一些点，我们用数组coordinates来分别记录它们的坐标，
# 其中coordinates[i] = [x, y]表示横坐标为 x、纵坐标为 y的点。
# 请你来判断，这些点是否在该坐标系中属于同一条直线上，是则返回 true，否则请返回 false。
from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        # 两点式： (y-y2)/(y1-y2)=(x-x2)/(x1-x2)
        # a = y2 - y1; b = x1 - x2; c = x2y1 - x1y2
        a = coordinates[1][1]-coordinates[0][1]
        b = coordinates[0][0]-coordinates[1][0]
        c = coordinates[1][0]*coordinates[0][1]-coordinates[0][0]*coordinates[1][1]
        for i in range(1, len(coordinates)):
            if coordinates[i][0]*a+coordinates[i][1]*b+c != 0:
                return False
        return True

