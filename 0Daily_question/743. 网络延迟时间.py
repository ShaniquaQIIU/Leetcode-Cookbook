#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/8/2 17:29
# @Author  : Shaniqua Qiu
# @File    : 743. 网络延迟时间.py

# https://leetcode-cn.com/problems/network-delay-time/
# 有 n 个网络节点，标记为 1 到 n。
# 给你一个列表 times，表示信号经过 有向 边的传递时间。 times[i] = (ui, vi, wi)，其中 ui 是源节点，vi 是目标节点， wi 是一个信号从源节点传递到目标节点的时间。
# 现在，从某个节点 K 发出一个信号。需要多久才能使所有节点都收到信号？如果不能使所有节点收到信号，返回 -1 。

from typing import List
from collections import deque


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """广度优先搜索"""
        # 建图 - 邻接表
        mp = [{} for i in range(n + 1)]
        for u, v, t in times:
            mp[u][v] = t
        # 记录结点最早收到信号的时间
        r = [-1 for i in range(n + 1)]
        r[k] = 0
        # 队列中存放 [结点，收到信号时间]
        s = deque([[k, 0]])
        while s:
            cur, t = s.popleft()
            for u, v in mp[cur].items():
                art = t + v
                # 仅当结点未收到或收到时间比记录时间更早才更新并入队
                if r[u] == -1 or art < r[u]:
                    r[u] = art
                    s.append([u, art])
        minT = -1
        for i in range(1, n + 1):
            if r[i] == -1:
                return -1
            minT = max(minT, r[i])
        return minT