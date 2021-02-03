#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/3 15:33
# @Author  : Shaniqua Qiu
# @File    : 424. 替换后的最长重复字符.py

# 2021-02-02 每日一题
from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # 动态滑动窗口
        maxLen, windowStart, maxFreq = 0, 0, 0
        # 统计出现频率
        freqDict = defaultdict(int)
        for windowEnd in range(len(s)):
            rightChar = s[windowEnd]
            freqDict[rightChar] += 1
            # 保存历史出现的最大频率
            maxFreq = max(freqDict[rightChar], maxFreq)
            # 缩小滑动窗口
            if (windowEnd - windowStart + 1 - maxFreq) > k:
                leftChar = s[windowStart]
                windowStart += 1
                freqDict[leftChar] -= 1
            maxLen = max(maxLen, windowEnd - windowStart + 1)
        return maxLen