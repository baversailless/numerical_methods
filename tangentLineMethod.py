import math


def f(x):
    return x**4 + x**2 + x + 1


def ff(x):
    return 4*x**3 + 2*x + 1


eps = 0.01
a = -1
b = 2
n = 0
x = (b*ff(b) - a*ff(a) + f(a) - f(b))/(ff(b)-ff(a))


def printFunction():
    print("n = ", n)
    print("a = ", a)
    print("b = ", b)
    print("x = ", x)
    print("ff(x) = ", ff(x))
    print("f(x) = ", f(x))
    print()
    print()


if ff(a)*ff(b) < 0:
    while abs(ff(x)) > eps:
        x = (b*ff(b) - a*ff(a) + f(a) - f(b))/(ff(b)-ff(a))
        printFunction()
        n = n + 1
        if ff(x) > 0 or ff(x) == 0:
            b = x
        elif ff(x) < 0:
            a = x
else:
    if (ff(a) > 0 and ff(b) > 0) or ff(a) == 0:
        x = a
    if (ff(a) < 0 and ff(b) < 0) or ff(b) == 0:
        x = b
