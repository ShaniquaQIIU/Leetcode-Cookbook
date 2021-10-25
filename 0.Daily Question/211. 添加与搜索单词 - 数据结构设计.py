#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/19 11:55
# @Author  : Shaniqua Qiu
# @File    : 211. 添加与搜索单词 - 数据结构设计.py


# https://leetcode-cn.com/problems/design-add-and-search-words-data-structure/
# 请你设计一个数据结构，支持 添加新单词 和 查找字符串是否与任何先前添加的字符串匹配 。
# 实现词典类 WordDictionary ：
# WordDictionary() 初始化词典对象
# void addWord(word) 将 word 添加到数据结构中，之后可以对它进行匹配
# bool search(word) 如果数据结构中存在字符串与 word 匹配，则返回 true ；否则，返回  false 。word 中可能包含一些 '.' ，每个 . 都可以表示任何一个字母。

from collections import deque


class WordDictionary:

    def __init__(self):
        self.trie = dict()

    def addWord(self, word: str) -> None:
        cur = self.trie
        for c in word:
            if c in cur:
                cur = cur[c]
            else:
                cur[c] = {}
                cur = cur[c]
        cur["#"] = {}

    def search(self, word: str) -> bool:
        word += "#"
        bfs = deque([(0, self.trie)])
        while bfs:
            idx, cur = bfs.pop()
            if idx == len(word):
                return True
            if word[idx] == '.':
                for nxt in cur.values():
                    bfs.append((idx+1,nxt))
            elif word[idx] in cur:
                bfs.append((idx+1,cur[word[idx]]))
        return False


if __name__ == '__main__':
    wordDictionary = WordDictionary()
    wordDictionary.addWord("bad")
    wordDictionary.addWord("dad")
    wordDictionary.addWord("mad")
    wordDictionary.search("pad")
    wordDictionary.search("bad")
    wordDictionary.search(".ad")
    wordDictionary.search("b..")
