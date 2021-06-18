#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/4 14:24
# @Author  : Shaniqua Qiu
# @File    : 86. 分隔链表.py

# 给你一个链表和一个特定值 x ，请你对链表进行分隔，使得所有小于 x 的节点都出现在大于或等于 x 的节点之前。
# 你应当保留两个分区中每个节点的初始相对位置。


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        cur = ListNode(-1)
        nxt = ListNode(-1)
        p1 = cur
        p2 = nxt
        while head:
            if head.val < x:
                p1.next = head
                p1 = p1.next
            else:
                p2.next = head
                p2 = p2.next
            head = head.next
        p1.next = nxt.next
        p2.next = None
        return cur.next