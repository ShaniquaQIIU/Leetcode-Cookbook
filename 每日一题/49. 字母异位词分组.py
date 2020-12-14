#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/14 09:20
# @Author  : Shaniqua Qiu
# @File    : 49. 字母异位词分组.py

# 2020-12-14
# 给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        dic = {}
        for s in strs:
            keys = "".join(sorted(s))
            if keys not in dic:
                dic[keys] = [s]
            else:
                dic[keys].append(s)
        return list(dic.values())