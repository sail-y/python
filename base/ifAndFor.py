#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 条件语句
age = 20
if age >= 6:
    print 'teenager'
elif age >= 18:
    print 'adult'
else:
    print 'kid'


if None:
	print 'None'

# 循环
sum = 0
for x in range(101):
    sum = sum + x
print sum

# while 循环

sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print sum

# raw_input
birth = int(raw_input('birth: '))
if birth < 2000:
    print '00前'
else:
    print '00后'