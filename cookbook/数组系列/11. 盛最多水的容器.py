#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/1 22:01
# @Author  : Shaniqua Qiu
# @File    : 11. 盛最多水的容器.py

# 给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。
# 在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0) 。
# 找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
# 说明：你不能倾斜容器。

from typing import List

# 使用内置函数效率低
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 双指针法
        res = 0
        left = 0
        right = len(height)-1
        while(left<right):
            min_hight = min(height[left], height[right])
            res = max(res, min_hight * (right - left))
            if min_hight == height[left]:
                left += 1
            else:
                right -=1
        return res


# 优化后
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 双指针法
        res = 0
        left = 0
        right = len(height)-1
        while(left<right):
            width = right - left
            if (height[left]< height[right]):
                min_hight = height[left]
                left += 1
            else:
                min_hight = height[right]
                right -=1
            res = res if res > min_hight * width  else  min_hight * width
        return res