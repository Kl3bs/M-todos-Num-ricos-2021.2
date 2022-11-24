import matplotlib.pyplot as plt
import numpy as np


def f(x):
    y = x
    return y


def plotFunctionAndPoints(a, b, points):
    points = np.array(points)
    x = np.linspace(a, b)

    plt.plot(x, f(x), color='red')
    plt.plot(points, points, 'bo', markersize=3, color='purple')

    plt.xlim(a, b)
    plt.ylim(a, b)

    plt.show()


points = [[0, 1], [1, 3], [1, 4], [3, 4]]
plotFunctionAndPoints(0, 10, points)
