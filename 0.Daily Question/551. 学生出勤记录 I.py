#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/8/17 09:42
# @Author  : Shaniqua Qiu
# @File    : 551. 学生出勤记录 I.py

# 给你一个字符串 s 表示一个学生的出勤记录，其中的每个字符用来标记当天的出勤情况（缺勤、迟到、到场）。记录中只含下面三种字符：
# 'A'：Absent，缺勤
# 'L'：Late，迟到
# 'P'：Present，到场
# 如果学生能够 同时 满足下面两个条件，则可以获得出勤奖励：
# 按 总出勤 计，学生缺勤（'A'）严格 少于两天。
# 学生 不会 存在 连续 3 天或 3 天以上的迟到（'L'）记录。
# 如果学生可以获得出勤奖励，返回 true ；否则，返回 false 。

class Solution:
    def checkRecord(self, s: str) -> bool:
        return s.count('A') <= 1 and "LLL" not in s
