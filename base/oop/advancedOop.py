#!/usr/bin/env python
# -*- coding: utf-8 -*-
'面向对象高级编程'
from types import MethodType


# 动态函数和属性
class Student(object):
    pass


def set_age(self, age):  # 定义一个函数作为实例方法
    self.age = age


s = Student()
s.name = 'Teddy'

print s.name
s.set_age = MethodType(set_age, s, Student)  # 给实例绑定一个方法
s.set_age(25)  # 调用实例方法
print s.age  # 测试结果


# 给所有实例都绑定方法，可以给class绑定方法：
def set_score(self, score):
    self.score = score


Student.set_score = MethodType(set_score, None, Student)

s.set_score(100)
print s.score


# 使用__slots__
# __slots__定义的属性仅对当前类起作用，对继承的子类是不起作用的：
class Student(object):
    __slots__ = ('name', 'age')  # 用tuple定义允许绑定的属性名称


# 使用@property
class Student(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value


s = Student()
s.score = 60  # OK，实际转化为s.set_score(60)
s.score  # OK，实际转化为s.get_score()
