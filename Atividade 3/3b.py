from sympy import *
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


def solveFunction(expression, a, b, points):
    x = symbols('x')
    res = sympify(expression)
    res = res.subs(x, a)
    return res


solveFunction("2*x+5", 1)
