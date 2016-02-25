# coding=utf-8
__author__ = 'xiaomai'


# 生成器

g = (x * x for x in range(10))
for n in g:
    pass
    # print n


# 如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator：
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n += 1


for n in fib(12):
    print n


def triangles():
    a = [1]
    while True:
        yield a

        a = [sum(i) for i in zip([0] + a, a + [0])]


g = triangles()
for n in range(10):
    print(next(g))
    # next(g)
