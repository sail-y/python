#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math

def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

print(my_abs(-12))

# 函数返回多个值



def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

r = move(100, 100, 60, math.pi / 6)

print r

def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print power(5)
print power(5, 5)

# 参数默认值
def enroll(name, gender, age=6, city='Beijing'):
    print 'name:', name
    print 'gender:', gender
    print 'age:', age
    print 'city:', city

#enroll('Adam', 'M', city='Tianjin')


# 默认参数必须指向不变对象！否则有巨坑
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
# 可变参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print calc(1, 3, 5, 7)
nums = [1, 2, 3]
calc(*nums)

#关键字参数
def person(name, age, **kw):
    print 'name:', name, 'age:', age, 'other:', kw

person('Adam', 45, gender='M', job='Engineer')

#参数组合
#在Python中定义函数，可以用必选参数、默认参数、可变参数和关键字参数，这4种参数都可以一起使用，或者只用其中某些，但是请注意
#参数定义的顺序必须是：必选参数、默认参数、可变参数和关键字参数。

def func(a, b, c=0, *args, **kw):
    print 'a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw
func(1, 2, 3, 'a', 'b', x=99)
args = (1, 2, 3, 4, 5)
kw = {'x': 99}
func(*args, **kw)

#递归函数
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)
print fact(6)
#尾递归
def fact(n):
    return fact_iter(1, 1, n)

def fact_iter(product, count, max):
    if count > max:
        return product
    return fact_iter(product * count, count + 1, max)
print fact(6)