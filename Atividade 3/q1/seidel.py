
from __future__ import division
import numpy as np
from numpy import linalg


def gauss_seidel(A, b, x0, tol, N):
    A = A.astype('double')
    b = b.astype('double')
    x0 = x0.astype('double')

    n = np.shape(A)[0]
    x = np.copy(x0)
    it = 0

    while (it < N):
        it = it+1

        for i in np.arange(n):
            x[i] = b[i]
            for j in np.concatenate((np.arange(0, i), np.arange(i+1, n))):
                x[i] -= A[i, j]*x[j]
            x[i] /= A[i, i]

        if (np.linalg.norm(x-x0, np.inf) < tol):
            return x

        x0 = np.copy(x)


A = np.array([[10, 2, 1],
             [1, 5, 1],
             [2, 3, 10],
              ])

b = np.array([7, -8, 6])

print(gauss_seidel(A, b, np.zeros(len(A)), 100000, len(A[0])))
