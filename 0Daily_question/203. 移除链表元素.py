#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/5Study_plan 19:44
# @Author  : Shaniqua Qiu
# @File    : 203. 移除链表元素.py

# 给你一个链表的头节点 head 和一个整数 val ，请你删除链表中所有满足 Node.val == val 的节点，并返回 新的头节点 。


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        tmp = ret = ListNode()
        while head:
            if head.val != val:
                tmp.next = head
                tmp = tmp.next
            head = head.next
        tmp.next = None
        return ret.next