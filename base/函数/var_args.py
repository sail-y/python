# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 函数的参数

# 默认参数
def power(x, n=2):
    s = 1
    while n > 0:
        n -= 1
        s = s * x
    return s


# print power(5, 2)
# print power(10)


def enroll(name, gender, age=6, city='beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)


# enroll('Sarah', 'F')
# enroll('Sarah', 'F', city='chengdu')


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


# print calc(1, 3, 5, 7)
nums = [1, 2, 3]


# print calc(*nums)

# 关键字参数

def person(name, age, **kw):
    print 'name:', name, 'age:', age, 'other:', kw


# person('Adam', 45, gender='M', job='Engineer')

extra = {'city': 'Beijing', 'job': 'Engineer'}


# kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。
# person('Jack', 24, **extra)

# 参数组合
# 在Python中定义函数，可以用必选参数、默认参数、可变参数和关键字参数，这4种参数都可以一起使用，或者只用其中某些，但是请注意
# 参数定义的顺序必须是：必选参数、默认参数、可变参数和关键字参数。

def func(a, b, c=0, *args, **kw):
    print 'a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw


func(1, 2, 3, 'a', 'b', x=99)
args = (1, 2, 3, 4, 5)
kw = {'x': 99}
func(*args, **kw)
