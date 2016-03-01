# coding=utf-8
__author__ = 'xiaomai'

with open('/Users/xiaomai/Downloads/ip-down', 'r') as f:
    for line in f.readlines():
        print(line.strip())  # 把末尾的'\n'删掉


f = open('/Users/xiaomai/Downloads/144.png', 'rb')
# print(f.read())


with open('/Users/xiaomai/test.txt', 'w') as f:
    f.write('Hello, world!')
