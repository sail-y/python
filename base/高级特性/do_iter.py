# coding=utf-8
__author__ = 'xiaomai'


# 迭代

d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print key
    print d[key]

for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)


from collections import Iterator

isinstance((x for x in range(10)), Iterator)