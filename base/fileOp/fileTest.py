#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'xiaomai'


f = open('/Users/xiaomai/test.txt', 'r')
for line in f.readlines():
    print(line.strip()) # 把末尾的'\n'删掉
f.close()

try:
    f = open('/Users/xiaomai/test.txt', 'r')
    print f.read()
finally:
    if f:
        f.close()

# with语句来自动帮我们调用close()方法：
with open('/Users/xiaomai/test.txt', 'r') as f:
    print f.read()



# 读取图片和视频等

f = open('/Users/xiaomai/Desktop/avatar.jpg', 'rb')
f.read()


import codecs
with codecs.open('/Users/xiaomai/testUTF.txt', 'r', 'utf-8') as f:
    print f.read() # u'\u6d4b\u8bd5'

f = open('/Users/xiaomai/test.txt', 'w')
f.write('Hello, world!')
f.close()

with open('/Users/xiaomai/test.txt', 'w') as f:
    f.write('Hello, world!')
