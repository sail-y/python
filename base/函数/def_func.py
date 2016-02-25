# coding=utf-8
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


# 解方程
def quadratic(a, b, c):
    if not isinstance(a, (int, float)) and isinstance(a, (int, float)) and isinstance(a, (int, float)):
        raise TypeError('bad operand type')
    if b * b - 4 * a * c < 0:
        return None
    else:
        x1 = (-b + math.sqrt(b * b - 4 * a * c)) / (2 * a)
        x2 = (-b - math.sqrt(b * b - 4 * a * c)) / (2 * a)
        return x1, x2


print(quadratic(2, 3, 1))  # => (-0.5, -1.0)
print(quadratic(1, 3, -4))  # => (1.0, -4.0)
