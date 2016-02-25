# coding=utf-8
__author__ = 'xiaomai'


# 递归函数
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


print fact(10)


# 尾递归
def fact1(n):
    return fact_iter(1, 1, n)


def fact_iter(product, count, max):
    if count > max:
        return product
    return fact_iter(product * count, count + 1, max)


print fact1(100)


def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        move(n - 1, a, c, b)  # 将前n-1个盘子从a移动到b上
        move(1, a, b, c)  # 将最底下的最后一个盘子从a移动到c上
        move(n - 1, b, a, c)  # 将b上的n-1个盘子移动到c上


move(3, 'A', 'B', 'C')
