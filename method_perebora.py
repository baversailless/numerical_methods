def function(x):
 return x + 2/x
a = 1
b = 2
eps = 0.005
n = (b-a)/eps
h = (b-a)/n
x = []
y = []
n = int(n)
for i in range(0, n):
 x.append(a + i*h)
for i in range(0, n):
 y.append(function(x[i]))
for i in range(0, n):
 print("x[", i, "] = ", round(x[i], 4),
 " " "y[", i, "] = ", round(y[i], 4))
print("The minimum f(x) = ", min(y))
for i in range(0, n):
 if y[i] == min(y):
 index = i
 break
print("The minimum x = ", x[index])