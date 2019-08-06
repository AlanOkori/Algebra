from numpy import * 
import numpy as np
from sympy import *

def gaussjordan(a,b): #inversa
    n=len(b)
    c=np.concatenate([a,b],axis=1)
    for e in range(n):
        t=c[e,e]
        for j in range(e, n+1):
            c[e,j]=c[e,j]/t
        for i in range(n):
            if i!=e:
                t=c[i,e]
                for j in range(e,n+1):
                    c[i,j]=c[i,j]-t*c[e,j]
    x=c[:,n]
    return x
    
def gaussjordan2(a,b):
    n=len(b)
    c=np.concatenate([a,b],axis=1)
    for e in range(n):
        c[e,e:]=c[e,e:]/c[e,e]
        for i in range(n):
            if i!=e:
                c[i,e:]=c[i,e:]-c[i,e]*c[e,e:]
    x=c[:,n]
    return x
    
def Inversa(a,b): #inversa
    n=len(b)
    I=np.identity(n)
    c=np.concatenate([a,b],axis=1)
    c=np.concatenate([c,I],axis=1)
    n=len(c)
    for e in range(n):
        t=c[e,e]
        for j in range(e, 2*n+1):
            c[e,j]=c[e,j]/t
        for i in range(n):
            if i!=e:
                t=c[i,e]
                for j in range(e,2*n+1):
                    c[i,j]=c[i,j]-t*c[e,j]
    x=c[:, n+1:]
    return x
    
def gauss(a,b):
    n=len(b)
    c=np.concatenate([a,b], axis=1)
    for e in range (n):
        t=c[e,e]
        for j in range(e,n+1):
            c[e,j]=c[e,j]/t 
        for i in range (e, n):
            if i!=e:
                t=c[i,e]
                for j in range(e, n+1):
                    c[i, j]=c[i, j]-t*c[e,j] #Reducir otras filas
    for e in range (n):
        t=c[e,e]
        for j in range(e+1,n+1):
            c[e,j]=c[e,j]/t #Normalizar fila e
        for i in range (n):
            if i!=e:
                t=c[i,e]
                for j in range(e+1, n+1):
                    c[i, j]=c[i, j]-t*c[e,j] #Reducir otras filas
    return x
def gauss1(a,b):
    n = len(b)
    c = np.concatenate([a,b], axis = 1) #matriz aumentada
    for e in range(n):
        t=c[e,e]
        for j in range(e, n+1): #Normalizar fila e
            c[e,j]=c[e,j]/t
        for i in range(e+1,n): #reducir filas debajo
            t = c[i,e]
            for j in range (e, n+1):
                c[i,j]=c[i,j]-t*c[e,j]
    x=np.zeros([n,1]) # Celdas para el vector X
    x[n-1]=c[n-1,n]
    for i in range (n-2,-1,-1): #Sistema triangular
        s=0
        for j in range(i+1,n):
            s=s+c[i,j]*x[j]
        x[i]=c[i,n]-s
    return x
 
def jacobi(a,b,x):
    n=len(x)
    t=x.copy()
    for i in range(n):
        s=0
        for j in range(n):
            if i!=j:
                s=s+a[i,j]*t[j]
        x[i]=(b[i]-s)/a[i,i]
    return x
    
def jacobi2(a,b,x,e,m):
    n=len(x)
    t=x.copy()
    for k in range(m):
        x=jacobi(a,b,x)
        d=np.linalg.norm(array(x)-array(t),inf)
        if d<e:
            return[x,k]
        else:
            t=x.copy()
    return [[],m]

def GaussSeidel(a,b,x):
    n=len(x)
    for i in range(n):
        s=0
        for j in range(n):
            if i!=j:
                s=s+a[i,j]*x[j]
        x[i]=(b[i]-s)/a[i,i]
    return x

def GaussSeidel2(a,b,x,e,m):
    n=len(x)
    t=x.copy()
    for k in range(m):
        x=GaussSeidel(a,b,x)
        d=np.linalg.norm(array(x)-array(t),inf)
        if d<e:
            return[x,k]
        else:
            t=x.copy()
    return [[],m]
    
    #Interpolación 
def lagrange(x,y,u=None):
    n=len(x)
    t=Symbol('t')
    p=0
    for i in range(n):
        L=1
        for j in range(n):
            if j!=i:
                L=L*(t-x[j])/(x[i]-x[j])
        p=p+y[i]*L
        p=expand(p)
    if u==None:
        return p
    elif type(u)==list:
        v=[]
        for i in range(len(u)):
            v=v+[p.subs(t,u[i])]
        return v
    else:
        return p.subs(t,u)