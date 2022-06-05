import math


def f(x):
    return x**2 + math.exp(-x)


def ff(x):
    return 2*x-math.exp(-x)


def sf(x):
    return 2 + math.exp(-x)


def printFunction():
    print("n = ", n)
    print("x = ", x)
    print("f(x) = ", f(x))
    print()
    print()


x = 0
n = 0
while abs(ff(x)) > 0.0001:
    printFunction()
    n = n+1
    x0 = x - (ff(x)/sf(x))
    x = x0
