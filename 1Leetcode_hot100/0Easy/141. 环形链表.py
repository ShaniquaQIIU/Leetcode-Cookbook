#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/13 13:48
# @Author  : Shaniqua Qiu
# @File    : 141. 环形链表.py

# 给定一个链表，判断链表中是否有环。
# 快慢指针
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        return True
