import numpy as np
import math
 
def cholesky(a):
    n = len(a)
    for k in range(n):
        try:
            a[k,k] = math.sqrt(a[k,k] \
            - np.dot(a[k,0:k],a[k,0:k]))
        except ValueError:
            print('Matrix is not positive definite')
        for i in range(k+1,n):
            a[i,k] = (a[i,k] - np.dot(a[i,0:k],a[k,0:k]))/a[k,k]
        
    for k in range(1,n): a[0:k,k] = 0.0
    
    print(a)
    return a



def choleskySol(L,b):
    n = len(b)
    
    for k in range(n):
        b[k] = (b[k] - np.dot(L[k,0:k],b[0:k]))/L[k,k]
         
    for k in range(n-1,-1,-1):
        b[k] = (b[k] - np.dot(L[k+1:n,k],b[k+1:n]))/L[k,k]
    return b

a  = np.array([[1,1,0], [1, 2, -1],[0, -1, 3]])
b = np.array([1, 1, 2])


print(choleskySol(cholesky(a), b))