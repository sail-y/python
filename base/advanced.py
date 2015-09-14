#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import Iterable

# 切片
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
# L[0:3]表示，从索引0开始取，直到索引3为止，但不包括索引3
print L[0:3]
# 如果第一个索引是0，还可以省略：
print L[:3]
# 倒数切片
print L[-2:-1]

L = range(100)
# 前10个数，每两个取一个：

print L[:10:2]
print L[10:50:9]
# tuple 和字符串也可以切片

# 迭代
print '迭代'

d = {'a': 1, 'b': 2, 'c': 3}
for k, v in d.iteritems():
    print k, v

isinstance([1, 2, 3], Iterable)

for i, value in enumerate(['A', 'B', 'C']):
    print i, value
# 2个变量
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print x, y
for r in [(1, 1), (2, 4), (3, 9)]:
    print r

# 列表生成式

[x * x for x in range(1, 11)]
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# 还可以使用两层循环，可以生成全排列：
[m + n for m in 'ABC' for n in 'XYZ']
[x + x for x in range(1, 11) if x % 2 == 0]

import os

[d for d in os.listdir('.')]

# 生成器（Generator）
g = (x * x for x in range(10))


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1


for n in fib(10):
    print n
