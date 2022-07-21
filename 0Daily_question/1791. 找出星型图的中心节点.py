#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/2/18 16:14
# @Author  : Shaniqua Qiu
# @File    : 1791. 找出星型图的中心节点.py

# 有一个无向的 星型 图，由 n 个编号从 1 到 n 的节点组成。星型图有一个 中心 节点，并且恰有 n - 1 条边将中心节点与其他每个节点连接起来。
# 给你一个二维整数数组 edges ，其中 edges[i] = [ui, vi] 表示在节点 ui 和 vi 之间存在一条边。请你找出并返回 edges 所表示星型图的中心节点。
# 链接：https://leetcode-cn.com/problems/find-center-of-star-graph

from typing import List


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        # 判断前两条边的公共定点
        if edges[1][0] in edges[0]:
            return  edges[1][0]
        else:
            return  edges[1][1]