 #!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/6 21:21
# @Author  : Shaniqua Qiu
# @File    : 136.只出现一次的数字

# 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = nums[0];
        size = len(nums)
        if size > 1:
            for i in range(size):
                ans = ans ^ nums[i];    # 异或
        return ans;


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return sum(set(nums)) *2 - sum(nums)