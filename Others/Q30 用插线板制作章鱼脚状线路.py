#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/3 10:12
# @Author  : Shaniqua Qiu
# @File    : Q30 用插线板制作章鱼脚状线路.py


def set_tap(remain):
    if dp[remain]:
        return dp[remain]
    cnt = 0
    # 2 个插口
    i = 1
    while i <= remain / 2:
        if remain - i == i:
            cnt += set_tap(i) * (set_tap(i) + 1) / 2
        else:
            cnt += set_tap(remain - i) * set_tap(i)
        i += 1
    # 3 个插口
    i = 1
    while i <= remain / 3:
        j = i
        while j <= (remain - i) / 2:
            if (remain - (i + j) == i) and (i == j):
                cnt += set_tap(i) * (set_tap(i) + 1) * (set_tap(i) + 2) / 6
            elif remain - (i + j) == i:
                cnt += set_tap(i) * (set_tap(i) + 1) * set_tap(j) / 2
            elif i == j:
                cnt += set_tap(remain - (i+j)) * set_tap(i) * (set_tap(i)+1) / 2
            elif remain - (i + j) == j:
                cnt += set_tap(j) * (set_tap(j) + 1) * set_tap(i) / 2
            else:
                cnt += set_tap(remain - (i + j)) * set_tap(j) * set_tap(i)
            j += 1
        i += 1

    dp[remain] = cnt
    return cnt


N = 20
dp = [0 for _ in range(N + 1)]
dp[1] = 1

print(set_tap(N))