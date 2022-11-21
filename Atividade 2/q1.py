import numpy as np
import math
import time 
from math import sqrt
import matplotlib.pyplot as plt

"""**QUESTÃO 1**

Equações :
"""

def gaussElimination(a,b):
    start_time = time.time()
    n = len(b)
     
    for k in range(0,n-1):
        for i in range(k+1,n):
            if a[i,k] != 0.0:
                lam = a [i,k]/a[k,k]
                a[i,k+1:n] = a[i,k+1:n] - lam*a[k,k+1:n]
                b[i] = b[i] - lam*b[k]
    for k in range(n-1,-1,-1):
        b[k] = (b[k] - np.dot(a[k,k+1:n],b[k+1:n]))/a[k,k]
    
    return b,time.time() - start_time

def plu(A):
  
    L = np.zeros_like(A, dtype=float)
    U = np.zeros_like(A, dtype=float)
    N = np.size(A, 0)

    for k in range(N):
        L[k, k] = 1
        U[k, k] = A[k, k] - np.dot(L[k, :k], U[:k, k]) 
        for j in range(k+1, N):
            U[k, j] = A[k, j] - np.dot(L[k, :k], U[:k, j])
        for i in range(k+1, N):
            L[i, k] = (A[i, k] - np.dot(L[i, :k], U[:k, k])) / U[k, k]

    return L, U


def LUsolver(A, b):
    
    m = len(A) 
    L, U = plu(A) 
    x = np.zeros(b.size)  
    y = np.zeros(b.size) 
 
    for i in range(0, m, 1):
        y[i] = b[i] / L[i][i]
        for j in range(0, i, 1):
            y[i] -= y[j] * L[i][j]
     
    for i in range(m-1, -1, -1):
        x[i] = y[i] / U[i][i]
        for j in range(i-1, -1, -1):
            U[i] -= x[i] * U[i][j]
    return x

def cholesky(A,B):
    start_time = time.time()
    n = len(A)
    # Create zero matrix for L
    L = np.zeros(np.shape(A))
    # Perform the Cholesky decomposition
    for i in range(n):
        for k in range(i+1):
            tmp_sum = sum(L[i][j] * L[k][j] for j in range(k)) #this is the sum that appears in both formulas
            
            if i == k: # Diagonal elements
                L[i][k] = np.sqrt(A[i][i] - tmp_sum)
            else:
                # Off diagonal elements
                L[i][k] = (1.0 / L[k][k] * (A[i][k] - tmp_sum))    
    choleskySol(L, np.transpose(L), B)
    return time.time() - start_time
    

def choleskySol(L,U,b):
  L=np.array(L, float)
  U=np.array(U, float)
  b=np.array(b, float)

  n,_=np.shape(L)
  y=np.zeros(n)
  x=np.zeros(n)

# Forward substitution
  for i in range(n):
    sumj=0
    for j in range(i):
      sumj += L[i,j]*y[j]
    y[i]=(b[i]-sumj)/L[i,i]

# Backward substitution  
  for i in range(n-1, -1, -1):
    sumj=0
    for j in range(i+1,n):
      sumj += U[i,j] * x[j]
    x[i]=(y[i]-sumj)/U[i,i]
  return x
