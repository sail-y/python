# coding=utf-8
__author__ = 'xiaomai'

# 列表生成式

a = [x * x for x in range(1, 11) if x % 2 == 0]
print a

print [m + n for m in 'ABC' for n in 'XYZ']


import os

print [d for d in os.listdir('.')]


L = ['Hello', 'World', 18, 'Apple', None]

print [x.lower() for x in L if isinstance(x, str)]