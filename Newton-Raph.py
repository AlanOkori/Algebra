from numpy import *

def f(x):
    y = x**4 - 10*(x**3) + 3*(x**2) + x + 23
    return y
def Df(x) :
    z = 4*(x**3) - 30*(x**2) + 6*x + 1
    return z

P0 = float(input("please insert the initial aproximation: "))
Err = float(input("Insert the tolerable error: "))
i = 0
P = P0 - (f(P0)/Df(P0))
while abs(P - P0) > Err :
    P = P0 - (f(P0)/Df(P0))
    i = i+1
    P0 = P
print(P)
print ("The method succeed until ", i, "Iterations.")
    