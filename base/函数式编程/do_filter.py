__author__ = 'xiaomai'


def is_odd(n):
    return n % 2 == 1

list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))


def is_palindrome(n):
    s = str(n)
    return s == s[::-1]

output = filter(is_palindrome, range(1, 1000))
print(list(output))