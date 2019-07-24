from numpy import * 
import numpy as np

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