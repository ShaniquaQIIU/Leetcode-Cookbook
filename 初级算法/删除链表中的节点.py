#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/4 16:48
# @Author  : Shaniqua Qiu
# @File    : 237.删除链表中的节点.py

# 请编写一个函数，使其可以删除某个链表中给定的（非末尾）节点。传入函数的唯一参数为 要被删除的节点 。
# 输入：head = [4,5,1,9], node = 5   输出：[4,1,9]

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def __init__(self):
        self.head = None

    def initList(self, data):
        self.head = ListNode(data[0])
        r = self.head
        p = self.head
        # 逐个为 data 内的数据创建结点, 建立链表
        for i in data[1:]:
            node = ListNode(i)
            p.next = node
            p = p.next
        return r

    def printlist(self, head):
        if head == None: return
        node = head
        while node != None:
            print(node.val, end='')
            node = node.next

    def deleteNode(self, node: ListNode):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next


if __name__ == '__main__':
    head = [4,5,1,9]
    s = Solution()
    l =s.initList(head)
    s.printlist(l)
    res = s.deleteNode(5)
    print(res)