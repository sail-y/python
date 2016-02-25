# coding=utf-8
import functools

__author__ = 'xiaomai'



# 偏函数

int2 = functools.partial(int, base=2)
print int2('1000000')
