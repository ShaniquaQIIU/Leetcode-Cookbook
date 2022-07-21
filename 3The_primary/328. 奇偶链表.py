#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/24 17:46
# @Author  : Shaniqua Qiu
# @Site    : https://leetcode-cn.com/problems/odd-even-linked-list/
# @File    : 328. 奇偶链表.py

# 给定一个单链表，把所有的奇数节点和偶数节点分别排在一起。请注意，这里的奇数节点和偶数节点指的是节点编号的奇偶性，而不是节点的值的奇偶性。
# 请尝试使用原地算法完成。你的算法的空间复杂度应为 O(1)，时间复杂度应为 O(nodes)，nodes 为节点总数。


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        l1, l2 = head, head.next
        p1, p2 = l1, l2
        while p2 != None and p2.next:
            p1.next = p1.next.next
            p2.next = p2.next.next
            p1 = p1.next
            p2 = p2.next
        p1.next = l2
        return l1
