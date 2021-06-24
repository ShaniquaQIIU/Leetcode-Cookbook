#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/21 10:00
# @Author  : Shaniqua Qiu
# @Site    : https://leetcode-cn.com/problems/binary-watch/
# @File    : 401. 二进制手表.py

# 二进制手表顶部有 4 个 LED 代表 小时（0-11），底部的 6 个 LED 代表 分钟（0-59）。每个 LED 代表一个 0 或 1，最低位在右侧。
from typing import List


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        ans = []
        for i in range(1024):
            h, m = i>>6, i&0x3f
            if h<12 and m<60 and bin(i).count("1") == turnedOn:
                ans.append(f"{h}:{m:02d}")
        return ans
