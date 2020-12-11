#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/11 09:38
# @Author  : Shaniqua Qiu
# @File    : 649. Dota2 参议院.py

from collections import deque
from typing import List


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        queueR = deque()
        queueD = deque()
        n = len(senate)
        for i, c in enumerate(senate):
            if c == "R":
                queueR.append(i)
            else:
                queueD.append(i)

        while queueR and queueD:
            if queueR[0] < queueD[0]:
                queueD.popleft()
                queueR.append(queueR.popleft() + n)
            else:
                queueR.popleft()
                queueD.append(queueD.popleft() + n)

        return "Radiant" if queueR else "Dire"


if __name__ == "__main__":
    s = Solution()
    senate = 'RDDRRDRDRDDD'
    print(s.predictPartyVictory(senate))
