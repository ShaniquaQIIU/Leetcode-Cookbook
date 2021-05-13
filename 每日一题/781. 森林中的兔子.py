#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/6 10:57
# @Author  : Shaniqua Qiu
# @File    : 781. 森林中的兔子.py

# 森林中，每个兔子都有颜色。其中一些兔子（可能是全部）告诉你还有多少其他的兔子和自己有相同的颜色。
# 我们将这些回答放在 answers 数组里。返回森林中兔子的最少数量。
from typing import List
import collections


class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = collections.Counter(answers)
        return sum((count[x] + x) // (x + 1) * (x + 1) for x in count)

