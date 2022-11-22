import numpy as np
import scipy
import math


def isDiagonallyDominant(A):
    matrix = np.copy(A)
    diag = np.diag(A)
    np.fill_diagonal(matrix, 0)
    matrix = np.abs(matrix)
    col_values = matrix.sum(axis=1)

    for i in range(len(diag)):
        if (diag[i] <= col_values[i]):
            return False

    return True

# In[3]:


# Matriz A, Matriz b dos termos independentes e N o número de iterações e o erro
def jacobi(A, b, N, chute, erro=0.00000001):
    if (criterio_linhas(A) > 1):
        print("O sistema não converge para o método de Jacobi")
        return

    x = np.diag(A)  # recebe um vetor contendo a diagonal principal
    A = A - np.diagflat(x)  # Zera a diagonal principal de A

    # Para dividir todos os valores da matriz A pelos termos independentes
    for i in range(x.size):
        A[i] = A[i]/x[i]
        b[i] = b[i]/x[i]

    x = np.copy(chute)
    swap = np.zeros(x.size)

    A = A*-1

    for stop in range(N):
        for i in range(x.size):
            swap[i] = np.sum((A[i]*x))+(b[i])
        # Cálculo da tolerância ou erro
        print(f"Iteração {stop}: {swap}")
        if ((np.linalg.norm(swap) - np.linalg.norm(x)) < erro):
            return swap
        x = np.copy(swap)

    return x


A = np.array([[2, -1, 1],
             [2, 2, 2],
             [-1, -1, 2],
              ])

b = np.array([-1, 4, -5])

x0 = np.zeros(3)

print(criterio_linhas(A))
