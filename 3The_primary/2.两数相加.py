#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/29 10:27
# @Author  : Shaniqua Qiu
# @Site    : https://leetcode-cn.com/problems/add-two-numbers/
# @File    : 2.两数相加.py

# 给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。
# 请你将两个数相加，并以相同形式返回一个表示和的链表。
# 你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        count = 0
        ret = ListNode()
        tmp = ret
        while l1 or l2 or count:
            num = 0
            if l1:
                num += l1.val
                l1 = l1.next
            if l2:
                num += l2.val
                l2 = l2.next
            if count:
                num += count
                count -= 1
            count, num = divmod(num, 10)   # 商， 余数
            tmp.next = ListNode(num)
            tmp = tmp.next
        return ret.next