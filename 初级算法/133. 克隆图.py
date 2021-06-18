#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/15 17:33
# @Author  : Shaniqua Qiu
# @File    : 133. 克隆图.py

# 给你无向 连通 图中一个节点的引用，请你返回该图的 深拷贝（克隆）。
# 图中的每个节点都包含它的值 val（int） 和其邻居的列表（list[Node]）。
# class Node {
#     public int val;
#     public List<Node> neighbors;
# }
#
# 测试用例格式：
# 简单起见，每个节点的值都和它的索引相同。例如，第一个节点值为 1（val = 1），第二个节点值为 2（val = 2），以此类推。该图在测试用例中使用邻接列表表示。
# 邻接列表 是用于表示有限图的无序列表的集合。每个列表都描述了图中节点的邻居集。
# 给定节点将始终是图中的第一个节点（值为 1）。你必须将 给定节点的拷贝 作为对克隆图的引用返回。



# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        dct = {}

        def dfs(node):
            if node in dct:
                return dct[node]
            res = Node(node.val, [])
            dct[node] = res
            for i in node.neighbors:
                res.neighbors.append(dfs(i))
            return res

        return dfs(node)