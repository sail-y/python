#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 函数式编程

# 高阶函数
#既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。
# 传入函数

def add(x, y, f):
    return f(x) + f(y)

print add(-5, 6, abs)

# map/reduce
def f(x):
	return x * x;

print map(f, range(9))	

def fn(x, y):
     return x * 10 + y

print reduce(fn, [1, 3, 5, 7, 9])     


def f(s):
	return s[0].upper() + s[1:].lower()

# print map(f, ['adam', 'LISA', 'barT'])
print map(str.capitalize, ['adam', 'LISA', 'barT'])


print reduce(lambda x, y: x * y, [1,2,3,4,5])

# filter
def is_odd(n):
    return n % 2 == 1

print filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])
# 结果: [1, 5, 9, 15]

def not_empty(s):
    return s and s.strip()

print filter(not_empty, ['A', '', 'B', None, 'C', '  '])
# 结果: ['A', 'B', 'C']
def is_prime(s):
	for i in range(2,s):
		if s%i==0:
			return False
	return True
# print filter(is_prime, range(1, 101))


# sorted

def reversed_cmp(x, y):
    if x > y:
        return -1
    if x < y:
        return 1
    return 0
print sorted([36, 5, 12, 9, 21], reversed_cmp)    

# 函数作为返回值

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

print lazy_sum(1, 3, 5, 7, 9)();    

# 闭包
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()
print f1()
print f2()

# 匿名函数
map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])


# decorator
import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print 'call %s():' % func.__name__
        return func(*args, **kw)
    return wrapper

@log
def now():
    print '2013-12-25'

#now()        
log(now)()

# decorator本身需要传入参数
def log(text):
    def decorator(func):
    	@functools.wraps(func)
        def wrapper(*args, **kw):
            print '%s %s():' % (text, func.__name__)
            return func(*args, **kw)
        return wrapper
    return decorator
@log('execute')
def now():
    print '2013-12-25'
#now() 
log('当前时间')(now)()

# 练习，前后日志打印
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
    	print 'begin call %s():' % func.__name__
        f = func(*args, **kw)
        print 'end call %s():' % func.__name__        
        return f
    return wrapper
@log
def now():
    print '2013-12-25'

now()   

# 练习，可变参数decorator
def log(text=None):

    def decorator(func):
    	@functools.wraps(func)
        def wrapper(*args, **kw):
        	if text == None:
        		print '%s %s():' % ('no text', func.__name__)	
        	else:
				print '%s %s():' % (text, func.__name__)
				return func(*args, **kw)
		return wrapper
    return decorator
@log('execute')
def now():
    print '2013-12-25'

# 偏函数

int2 = functools.partial(int, base=2)
print int2('1000000')