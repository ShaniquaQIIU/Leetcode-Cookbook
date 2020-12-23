#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/23 13:52
# @Author  : Shaniqua Qiu
# @File    : 344. 反转字符串.py

# 编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 char[] 的形式给出。
# 不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。
# 你可以假设数组中的所有字符都是 ASCII 码表中的可打印字符。
# 输入：["h","e","l","l","o"]
# 输出：["o","l","l","e","h"]

from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s[:] = s[::-1]
