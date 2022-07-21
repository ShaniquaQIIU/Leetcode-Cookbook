#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/10 11:46
# @Author  : Shaniqua Qiu
# @File    : 19. 删除链表的倒数第N个节点.py

# 给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
# 给定一个链表: 1->2->3->4->5Study_plan, 和 n = 2.
# 当删除了倒数第二个节点后，链表变为 1->2->3->5Study_plan.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head:
            self.count = 0
            return head
        head.next = self.removeNthFromEnd(head.next, n)  # 递归调用
        self.count += 1  # 回溯时进行节点计数
        return head.next if self.count == n else head


# 2021-07-25
class Solution:
    cur = 0
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        left, right = head, head
        count = 0
        while count < n:
            right = right.next
            count += 1
        if not right:
            return head.next
        while right.next:
            left = left.next
            right = right.next
        if left.next:
            left.next = left.next.next
        return head
