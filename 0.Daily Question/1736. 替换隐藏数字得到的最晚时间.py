#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/26 10:30
# @Author  : Shaniqua Qiu
# @Site    : https://leetcode-cn.com/problems/latest-time-by-replacing-hidden-digits/
# @File    : 1736. 替换隐藏数字得到的最晚时间.py

# 给你一个字符串 time ，格式为 hh:mm（小时：分钟），其中某几位数字被隐藏（用 ? 表示）。
# 有效的时间为 00:00 到 23:59 之间的所有时间，包括 00:00 和 23:59 。
# 替换 time 中隐藏的数字，返回你可以得到的最晚有效时间。


class Solution:
    def maximumTime(self, time: str) -> str:
        time = list(time)
        a, b, c, d = time[0], time[1], time[3], time[4]
        if a == '?':
            time[0] = '2' if b in ('?', '0', '1', '2', '3') else '1'
        if b == '?':
            time[1] = '3' if time[0] == '2' else '9'
        if c == '?':
            time[3] = '5'
        if d == '?':
            time[4] = '9'

        return ''.join(time)