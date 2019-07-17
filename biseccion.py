from numpy import *

def f(x):
    y = x - sin(x)
    return y

x1 = float(input("Please enter the minimun value: "))
x2 = float(input("Please enter the maximum value: "))
err = float(input("Please insert the tolerable error: "))

r = (x1+x2)/2.0
i = 1

while abs(f(r)) > err:
    r = (x1+x2)/2.0
    if f(x1) * f(x2) > 0:
        x1 = r
    else:
        x2 = r
    i = i +1
print(r)
print ("The method succeed until ", i, "Iterations.")