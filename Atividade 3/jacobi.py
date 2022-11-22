import numpy as np


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


def jacobi(A, b, tolerance=1e-10, max_iterations=10000):

    if isDiagonallyDominant(A):
        A = A.astype('double')
        b = b.astype('double')

        # Create a copy of b with zeros
        x = np.zeros_like(b, dtype=np.double)

        # Replace the main diag wih 0
        T = A - np.diag(np.diagonal(A))

        for k in range(max_iterations):
            x_old = x.copy()
            x[:] = (b - np.dot(T, x)) / np.diagonal(A)

            if np.linalg.norm(x - x_old, ord=np.inf) / np.linalg.norm(x, ord=np.inf) < tolerance:
                break
        return x
    else:
        print("The system does not converge")
        return


# A
A = np.array([[4, 1, 0, 1, 0, 0],
             [-1, 4, -1, 0, -1, 0],
             [0, -1, 4, 0, 0, - 1],
             [-1, 0, 0, 4, -1, 0],
             [0, -1, 0, -1, 4, -1],
             [0, 0, -1, 0, -1, 4], ])

b = np.array([0, 5, 0, 6, -2, 6])

print(jacobi(A, b))


# B
A = np.array([[2, -1, 1],
             [2, 2, 2],
             [-1, -1, 2],
              ])

b = np.array([-1, 4, -5])

print(jacobi(A, b))


# c
A = np.array([[4, 1, -1, 1],
             [1, 4, -1, -1],
             [-1, -1, 5, 1],
             [1, -1, 1, 3],
              ])

b = np.array([-2, -1, 0, 1])

print(jacobi(A, b))
