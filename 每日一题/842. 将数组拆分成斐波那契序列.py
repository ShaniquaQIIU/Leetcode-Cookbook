#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/8 09:36
# @Author  : Shaniqua Qiu
# @File    : 842. 将数组拆分成斐波那契序列.py

# 给定一个数字字符串 S，比如 S = "123456579"，我们可以将它分成斐波那契式的序列 [123, 456, 579]。
# 对于所有的0 <= i < F.length - 2，都有 F[i] + F[i+1] = F[i+2] 成立。
# 每个块的数字不能以零开头
from typing import List


class Solution:
    # 回溯
    def splitIntoFibonacci(self, S: str) -> List[int]:
        def backtrack(cur, temp):
            if len(temp) >= 3 and cur == n:  # 退出条件
                self.res = temp
                return
            if cur == n:  # 剪枝
                return
            for i in range(cur, n):
                if S[cur] == "0" and i > cur:  # 当数字以0开头则跳过
                    return
                if int(S[cur: i+1]) > 2 ** 31 - 1 or int(S[cur: i+1]) < 0:  # 越界跳过
                    continue
                if len(temp) < 2:
                    backtrack(i+1, temp+[int(S[cur: i+1])])
                elif int(S[cur: i+1]) == temp[-1] + temp[-2]:
                    backtrack(i+1, temp + [int(S[cur: i+1])])

        n = len(S)
        self.res = []
        backtrack(0, [])
        return self.res



if __name__ == '__main__':
    s = Solution()
    S = '11001111'
    res = s.splitIntoFibonacci(S)
    print(res)

