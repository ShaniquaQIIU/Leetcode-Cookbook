#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/24 10:14
# @Author  : Shaniqua Qiu
# @File    : Q04 切分木棒.py

# 假设要把长度为 n 厘米的木棒切分为 1 厘米长的小段，但是 1 根木棒只能由 1 人切分，
# 当木棒被切分为 3 段后，可以同时由 3 个人分别切分木棒
# 求最多有 m 个人时，最少要切分几次。譬如 n ＝ 8，m＝ 3 时如图所示，切分 4 次就可以了

import math

# 计算公式
# 经观察可得，长度为n的木棒，切割后非叶节点有n-1个。
# 第一部分: i=logm+1  表示前i层的节点切分需要按层计算，即前2^i−1个节点需要切分i次。
# 第二部分: j = (n-1-(2^i-1))/m + 1  表示除去第一部分的节点剩余非叶节点的切分次数（每次切分都有m个人）

class Solution:
    def cutBar(self, n, m):
        return ((n-(n%m)-1)//m)+math.ceil(math.log(m+(n%m), 2))


if __name__ == '__main__':
    s = Solution()
    n, m = 20, 3
    res = s.cutBar(n, m)
    print(res)


