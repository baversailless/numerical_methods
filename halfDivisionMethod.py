a = 1
b = 2
eps = 0.0002
delta = 0.0001
n = 0


def function(x):
    return x + 1/pow(x, 2)


def printFunction():
    print("n = ", n)
    print("a = ", a)
    print("b = ", b)
    print("delta = ", delta)
    print("epsilon = ", eps)
    print("f* = ", function((a+b)/2))
    print("x* = ", (a+b)/2)
    print(" ")
    print(" ")


while(abs(b-a) > eps):
    printFunction()
    n = n + 1
    c = (a + b)/2
    x1 = c - delta/2
    x2 = c + delta/2
    if function(x1) < function(x2):
        b = x2
    else:
        a = x1
