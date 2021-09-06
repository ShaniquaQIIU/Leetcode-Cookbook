#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/9/6 19:34
# @Author  : Shaniqua Qiu
# @File    : 剑指 Offer 22. 链表中倒数第k个节点.py

# 输入一个链表，输出该链表中倒数第k个节点。为了符合大多数人的习惯，本题从1开始计数，即链表的尾节点是倒数第1个节点。
# 例如，一个链表有 6 个节点，从头节点开始，它们的值依次是 1、2、3、4、5、6。这个链表的倒数第 3 个节点是值为 4 的节点。


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        fast, slow = head, head
        for _ in range(k):
            fast = fast.next
        while fast:
            fast, slow = fast.next, slow.next
        return slow