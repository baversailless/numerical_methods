import math
import numpy as np


def f(x):
    return math.cos(x)/(x**2)


L = 0.02
a = 7
b = 11
eps = 0.01
n = 0
x_p = dict()


def d(x, p):
    return (f(x) - p)/(2*L)


def x1(x, p):
    return x - d(x, p)


def x2(x, p):
    return x + d(x, p)


def pp(x, p):
    return (f(x)-p)/2


def printFunction(x):
    print("n = ", n)
    print("x = ", x)
    print("p = ", p)
    print("err = ", err)
    print("f(x) = ", f(x))
    print()
    print()


x = (f(a) - f(b) + L*(a+b))/(2*L)
p = (f(a) + f(b) + L*(a-b))/2
err = 2*L*d(x, p)
x_p = {x1(x, p): pp(x, p), x2(x, p): pp(x, p)}

while err > eps:
    n = n + 1
    x_p = dict(sorted(x_p.items(), key=lambda x: x[1], reverse=True))
    print(x_p)
    xp = [list(x_p.keys())[-1], list(x_p.values())[-1]]
    x_p.popitem()
    x_p.update({x1(xp[0], xp[1]): pp(xp[0], xp[1]),
               x2(xp[0], xp[1]): pp(xp[0], xp[1])})

    printFunction(xp[0])
    err = abs(2*L*d(xp[0], xp[1]))
    print(err)
