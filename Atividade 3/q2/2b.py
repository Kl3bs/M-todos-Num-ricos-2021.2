import numpy as np
from numpy import linalg
import matplotlib.pyplot as plt


def mmq(points, n):
    points = np.array(points)
    x, y = points.T
    h = np.zeros((n+1, len(points)))

    for i in range(n+1):
        for j in range(len(points)):
            h[i][j] = pow(x[j], i)

     # Making the Ax = b system
    A = np.zeros((n+1, n+1))
    b = np.zeros(n+1)

    for i in range(len(A)):
        for j in range(len(A)):
            A[i][j] = h[i].dot(h[j])
        b[i] = h[i].dot(y)

    return np.linalg.solve(A, b)


points = [[1, 3], [2, 5], [3, 6], [4, 8], [-1, -3], [-2, -5], ]
mmq(points, 3)
