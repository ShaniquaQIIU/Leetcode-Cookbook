#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/27 09:57
# @Author  : Shaniqua Qiu
# @Site    : https://leetcode-cn.com/problems/second-minimum-node-in-a-binary-tree/
# @File    : 671. 二叉树中第二小的节点.py

# 给定一个非空特殊的二叉树，每个节点都是正数，并且每个节点的子节点数量只能为2或0。如果一个节点有两个子节点的话，那么该节点的值等于两个子节点中较小的一个。
# 更正式地说，root.val = min(root.left.val, root.right.val) 总成立。
# 给出这样的一个二叉树，你需要输出所有节点中的第二小的值。如果第二小的值不存在的话，输出 -1 。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        if not root or not root.left:
            return -1
        left = root.left.val if root.left.val != root.val else self.findSecondMinimumValue(root.left)
        right = root.right.val if root.right.val != root.val else self.findSecondMinimumValue(root.right)
        # 两个节点分别返回他们认为的第二小的值
        return min(left, right) if min(left, right) != -1 else max(right, left)
