#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/12 18:17
# @Author  : Shaniqua Qiu
# @File    : 234. 回文链表.py

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 用list做比较
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        vals = []
        while head is not None:
            vals.append(head.val)
            head = head.next
        return vals == vals[::-1]
