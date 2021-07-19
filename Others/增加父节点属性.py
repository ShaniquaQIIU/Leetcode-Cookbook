#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/13 16:47
# @Author  : Shaniqua Qiu
# @Site    : 
# @File    : 增加父节点属性.py

# // 1. 给一个树结构，每个节点包含 id 和 children（可能为 undefined） 两个属性，给每个子节点增加一个属性 parentId，值为其父节点的 id，并返回新生成的树。
# // 例如
# // 输入:
# // { id: 1, children: [{ id: 2 }, { id: 3, children: [{ id: 4 }] }] };
# // 输出:
# // { id: 1, children: [{ id: 2, parentId: 1 }, { id: 3, parentId: 1, children: [{ id: 4, parentId: 3 }] }] };


def addParentId(tree):
    if not tree or not tree.get('children'):   # 为空或者没有子节点
        return tree
    child = tree.get("children")
    parent = tree.get("id")
    for item in child:
        item["parentId"] = parent
        addParentId(item)
    return tree



if __name__ == "__main__":
    tree={ "id": 1, "children": [{ "id": 2 }, { "id": 3, "children": [{ "id": 4 }] }] }
    print(addParentId(tree))
