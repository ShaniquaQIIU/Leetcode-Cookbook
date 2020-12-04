#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/4 09:48
# @Author  : Shaniqua Qiu
# @File    : 659. 分割数组为连续子序列.py

import heapq
from collections import defaultdict
from typing import List

# 给你一个按升序排序的整数数组 num（可能包含重复数字），请你将它们分割成一个或多个子序列，其中每个子序列都由连续整数组成且长度至少为 3 。
# 如果可以完成上述分割，则返回 true ；否则，返回 false 。

# heapq有两种方式创建堆， 一种是使用一个空列表，然后使用heapq.heappush()函数把值加入堆中，
# 另外一种就是使用heap.heapify(list)转换列表成为堆结构
# python里通常创建的是最小堆, 对于最小堆来说, 堆中索引位置0即heap[0]的值一定是堆中的最小值,
# 并且堆中的每个元素都符合公式heap[k] <= heap[k*2+1]和 heap[k] <= heap[k*2+2], 其中heap[k]是父节点,
# 而heap[k*2+1]和heap[k*2+2]是heap[k]的子节点, 父节点永远小于等于它自己的子节点。
# heapq.heappop() 函数弹出堆中最小值

# defaultdict接受一个工厂函数作为参数，当key不存在时，返回的是工厂函数的默认值


# 每遍历一个数，将该数加入能加入的长度最短的序列中，不能加入序列则新建一个序列；然后更新字典
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        chains = defaultdict(list)

        for i in nums:
            if not chains[i - 1]:
                heapq.heappush(chains[i], 1)
            else:
                min_len = heapq.heappop(chains[i - 1])
                heapq.heappush(chains[i], min_len + 1)
            print(chains)
        for _, chain in chains.items():
            if chain and chain[0] < 3:
                return False
        return True

if __name__ == '__main__':
    s = Solution()
    nums = [1,2,3,3,3,4,5]
    s.isPossible(nums)

