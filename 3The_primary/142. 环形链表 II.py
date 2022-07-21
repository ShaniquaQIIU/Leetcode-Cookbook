#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/18 15:44
# @Author  : Shaniqua Qiu
# @File    : 142. 环形链表 II.py

# 给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
# 为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。注意，pos 仅仅是用于标识环的情况，并不会作为参数传递到函数中。
# 说明：不允许修改给定的链表。


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return None
        slow, fast = head, head
        while True:
            if not fast or not fast.next:
                return None
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break

        fast = head  # 第一次相遇后，快指针重新回到头节点
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow
