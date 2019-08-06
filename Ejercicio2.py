from numpy import *
from lineal import *

a=array([[1,1/2,1/3],[1/4,1/5,1/6],[1/7,1/8,1/9]],float)
b=array([[4],[5],[6]],float)
x=array([[121],[-666],[647]])

print(jacobi2(a,b,x,0.01,10050))