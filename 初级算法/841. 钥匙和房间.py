#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/11 14:38
# @Author  : Shaniqua Qiu
# @File    : 841. 钥匙和房间.py

# 有 N 个房间，开始时你位于 0 号房间。每个房间有不同的号码：0，1，2，...，N-1，并且房间里可能有一些钥匙能使你进入下一个房间。
# 在形式上，对于每个房间 i 都有一个钥匙列表 rooms[i]，每个钥匙 rooms[i][j] 由 [0,1，...，N-1] 中的一个整数表示，其中 N = rooms.length。 钥匙 rooms[i][j] = v 可以打开编号为 v 的房间。
# 最初，除 0 号房间外的其余所有房间都被锁住。
# 你可以自由地在房间之间来回走动。
# 如果能进入每个房间返回 true，否则返回 false。
from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited, stack = [0], [0]
        while stack:
            room_index = stack.pop()  # 房间号
            for key in rooms[room_index]:
                if key not in visited:  # 获取房间的钥匙
                    stack.append(key)
                    visited.append(key) # 可以访问的房间队列
        return len(visited) == len(rooms)

