import numpy as np
import math
a = 0
b = 1
eps = 0.0001
n = 0


def function(x):
    return 2*x+1/x


def printFunction():
    print("n = ", n)
    print("a = ", a)
    print("b = ", b)
    print("x* = ", (a+b)/2)
    print("f* =", function((a+b)/2))
    print("eps = ", eps)
    print(" ")


x1 = a + ((3 - math.sqrt(5))/2)*(b-a)
x2 = a + ((math.sqrt(5)-1)/2)*(b-a)

while(abs((b-a)/2) > eps):
    printFunction()
    n = n+1
    if function(x1) < function(x2):
        b = x2
        x2 = x1
        x1 = a + b - x2
    elif function(x1) > function(x2):
        a = x1
        x1 = x2
        x2 = b - x1 + a
