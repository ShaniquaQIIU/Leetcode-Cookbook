#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/15 16:52
# @Author  : Shaniqua Qiu
# @File    : 24. 两两交换链表中的节点.py

# https://leetcode-cn.com/problems/swap-nodes-in-pairs/
# 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        pre, pre.next = self, head
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            pre.next, b.next, a.next = b, a, b.next
            pre = a
        return self.next
