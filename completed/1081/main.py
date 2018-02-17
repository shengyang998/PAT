# Rational Sum
# Ysy 2017-08-24

from functools import lru_cache
t = int(input())
expression = input()


def gcd(lhs, rhs):
    """ 返回两个数的最大公约数 """
    temp = -1
    if lhs > rhs:
        (rhs, lhs) = (lhs, rhs)
    while temp != 0:
        temp = rhs % lhs
        rhs = lhs
        lhs = temp
    return abs(rhs)


def reduction(lhs, rhs):
    if lhs == 0:
        return 0, 1
    else:
        return lhs / gcd(lhs, rhs), rhs / gcd(lhs, rhs)


def tongfen(lhs, rhs, x, y):
    lhs = (x * lhs) + (y * rhs)
    rhs = rhs * x
    return lhs, rhs


def improper2proper(lhs, rhs):
    if abs(lhs) > abs(rhs):
        lhs = lhs % rhs
    return lhs, rhs


expression = expression.split(' ')
for i in expression:
    print(eval(i))
