#!/usr/bin/env pxthon
# -*- coding: utf-8 -*-
__author__ = 'xiaomai'
import os
print(os.name)

print(os.uname())

print(os.environ)
print(os.getenv('PATH'))

# 查看当前目录的绝对路径:
print os.path.abspath('.')
#'/Users/xiaomai'
# 在某个目录下创建一个新目录，
# 首先把新目录的完整路径表示出来:
print os.path.join('/Users/xiaomai', 'testdir')
#'/Users/michael/testdir'
# 然后创建一个目录:
os.mkdir('/Users/xiaomai/testdir')
# 删掉一个目录:
os.rmdir('/Users/xiaomai/testdir')

print([x for x in os.listdir('.') if os.path.isdir(x)])

print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.px'])
print('##########')
def search(dir, s):
    for x in os.listdir(dir):
        join = os.path.join(dir, x)
        if os.path.isfile(join) and s in os.path.splitext(x)[1]:
            print(join)
        if os.path.isdir(join):
            search(join, s)

search('/Users/xiaomai/code', '.java')