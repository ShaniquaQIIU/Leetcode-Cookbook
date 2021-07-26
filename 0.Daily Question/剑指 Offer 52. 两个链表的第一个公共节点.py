#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/21 09:47
# @Author  : Shaniqua Qiu
# @Site    : https://leetcode-cn.com/problems/liang-ge-lian-biao-de-di-yi-ge-gong-gong-jie-dian-lcof/
# @File    : 剑指 Offer 52. 两个链表的第一个公共节点.py

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        a, b = headA, headB
        while a != b:
            a = headB if a is None else a.next
            b = headA if b is None else b.next
        return a
