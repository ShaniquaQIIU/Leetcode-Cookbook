#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/12 11:18
# @Author  : Shaniqua Qiu
# @File    : 206. 反转链表.py

# 反转一个单链表。
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 思路：当前节点指向上一个节点；cur.next -> pre
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None
        cur = head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre
