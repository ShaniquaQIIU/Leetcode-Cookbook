#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/28 14:01
# @Author  : Shaniqua Qiu
# @File    : Q40 优雅的 IP 地址.py

# 2020-12-28
# 十进制数 0~9 这 10 个数字各出现 1 次的 IP 地址
# A.B.C.D 这种形式中，A 要和 D 对称，B 要和 C 对称。

hmap = {}
for i in range(256):   # 键值对形式将对称数据存到map中
    rev = int("0b"+("0"*8+bin(i)[2:])[-8:][::-1], base=2)
    list_i = list(str(i))
    list_rev = list(str(rev))
    if not [k for k in list_i if k in list_rev]:  # 初步过滤str重复的数据
        hmap[str(i)] = str(rev)

count = 0
for k1, v1 in hmap.items():
    for k2, v2 in hmap.items():
        ip_ads = k1 + '.' + k2 + '.' + v2 + '.' + v1
        if len(set(list(ip_ads))) == 11:  # 再次过滤str不重复的数据
            print(ip_ads)
            count += 1

print(count)
