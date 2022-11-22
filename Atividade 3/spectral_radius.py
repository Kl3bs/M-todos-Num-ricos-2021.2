
import numpy as np
from scipy import linalg


def convergenceTest(A):
    # Give 0 to all values outside of the diagonal
    D = np.zeros(np.shape(A))
    np.fill_diagonal(D, np.diag(A))

    # Setting the all diagonal values as 0
    R = A - D

    # Solving the system
    T = np.linalg.solve(-D, R)

    # Extracting the eignvalues
    eigsT, _ = np.linalg.eig(T)

    # Spectral radius
    rho = np.max(np.abs(eigsT))

    return rho


A = np.array([[4, 1, 0, 1, 0, 0],
             [-1, 4, -1, 0, -1, 0],
             [0, -1, 4, 0, 0, - 1],
             [-1, 0, 0, 4, -1, 0],
             [0, -1, 0, -1, 4, -1],
             [0, 0, -1, 0, -1, 4], ])
test(A)

# print(linalg.eigvals(A))

A = np.array([[2, -1, 1],
             [2, 2, 2],
             [-1, -1, 2],
              ])

test(A)
# print(linalg.eigvals(A))


A = np.array([[4, 1, -1, 1],
             [1, 4, -1, -1],
             [-1, -1, 5, 1],
             [1, -1, 1, 3],
              ])

test(A)
