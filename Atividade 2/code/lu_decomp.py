
import numpy as np # import the numpy library

def LU_decomposition(A):
  
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
    L, U = LU_decomposition(A)  
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
B =  generateRandomVector(n)





print(LUsolver(A, B))

for item in range:
    