import numpy as np
import math
 
 
def Cholesky(A):
    """Performs a Cholesky decomposition of A, which must 
    be a symmetric and positive definite matrix. The function
    returns the lower variant triangular matrix, L."""
    
    from math import sqrt
    
    n = len(A)

    # Create zero matrix for L
    L = np.zeros(np.shape(A))

    # Perform the Cholesky decomposition
    for i in range(n):
        for k in range(i+1):
            tmp_sum = sum(L[i][j] * L[k][j] for j in range(k)) #this is the sum that appears in both formulas
            
            if i == k: # Diagonal elements
                L[i][k] = sqrt(A[i][i] - tmp_sum)
            else:
                # Off diagonal elements
                L[i][k] = (1.0 / L[k][k] * (A[i][k] - tmp_sum))
                
    return L
    
# Now we define a function that solves our system using firstly forward substition and then backward
# It uses the matrix given from the first function, its transpose and B from Ax=B and provides the solution x

def solver(L,U,b):
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
    
# Finally, we constract matrix A (500x500)

def generateRandomMatrix(n, int_only):
    #n is the matrix size
    #int_only = True returns an integer SPD matrix, False is the default value
    if int_only == True:
        return np.random.randint(10, size=(n, n)) 
    return np.random.rand(n, n)

def generateSPD(n,int_only:bool=False):
    A = generateRandomMatrix(n, int_only)
    A_transpose = np.transpose(A)
    return np.dot(A, A_transpose)    

def generateRandomVector(n):
    return np.random.rand(n)


n = 3
A = generateSPD(n)

# And then B (500x1)

B =  generateRandomVector(n)

l = Cholesky(A)
U = np.transpose(l)
x = solver(l, U, B)

print(x)
# Now, we use the built-in function for Cholesky Decomposition to compare our results

from numpy.linalg import cholesky

L = cholesky(A)
U = np.transpose(L)
y = solver(L, U, B)

print(y)
