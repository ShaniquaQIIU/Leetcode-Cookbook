#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/6 21:49
# @Author  : Shaniqua Qiu
# @File    : 350.两个数组的交集 II

# 给定两个数组，编写一个函数来计算它们的交集。
from typing import List
from collections import Counter, defaultdict


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic1, dic2 = Counter(nums1), Counter(nums2)
        res=[]
        for i in dic1:  # key 判断是否有相同的值
            count = min(dic1[i], dic2[i])  # value  相同值重复几次
            num = [i] * count   # 交集放入结果
            res.extend(num)
        return res


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic1, dic2 = Counter(nums1), Counter(nums2)
        print(dic1, dic2)
        dct3 = {i: min(dic1[i], dic2[i]) for i in set(dic1)&set(dic2)}
        return sum([[key]*val for key, val in dct3.items()], [])

if __name__ == '__main__':
    s = Solution()
    nums1 = [1, 2, 3, 2, 1]
    nums2 = [1, 2, 2, 2, 3, 1, 2]
    print(s.intersect(nums1, nums2))