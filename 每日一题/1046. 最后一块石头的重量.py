#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/30 18:56
# @Author  : Shaniqua Qiu
# @File    : 1046. 最后一块石头的重量.py


# 每一回合，从中选出两块 最重的 石头，然后将它们一起粉碎。假设石头的重量分别为x 和y，且0x <= y。那么粉碎的可能结果如下：
# 如果x == y，那么两块石头都会被完全粉碎；
# 如果x != y，那么重量为x的石头将会完全粉碎，而重量为y的石头新重量为y-x。
# 最后，最多只会剩下一块石头。返回此石头的重量。如果没有石头剩下，就返回 0。
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones)>=2:
            stones.sort()
            stones.append(stones.pop()-stones.pop())
        return stones[0]