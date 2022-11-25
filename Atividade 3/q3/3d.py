import numpy as np
from sympy import *
import matplotlib.pyplot as plt


def solveFunction(expression, a):
    x = symbols('x')
    res = sympify(expression)
    res = res.subs(x, a)
    return res


def solveIntegral(function, a, b, n):
    h = (b-a)/n

    # f(a) + f(b)
    x1_0 = solveFunction(function, a) + solveFunction(function, b)
    x1_1 = 0
    x1_2 = 0

    for i in range(n-1):
        x = a + (i*h)
        if i % 2 == 0:
            x1_2 += solveFunction(function, x)
        else:
            x1_1 += solveFunction(function, x)

    x1 = (h*(x1_0 + 2*(x1_2) + 4*(x1_1)))/3
    return function, n, x1


def plotIntegralInfo(function, x, y):

    y = np.array(y)
    x = list(map(str, x))

    fig, ax = plt.subplots()

    ax.bar(x, y, width=0.5, edgecolor="white", linewidth=0.7, color='green')
    plt.xlabel('Valor de N')
    plt.ylabel('Resultado')
    plt.title(function)

    plt.show()


def getIntegralresults(function, n, result, n_list):

    for i in range(len(n)):
        integral = (solveIntegral(function, 0, 10, n[i]))
        result.append(integral[2])
        n_list.append(integral[1])

    return function, n_list, result


f = getIntegralresults("2*x+3", [2, 10, 200], [], [])
plotIntegralInfo(f[0], f[1], f[2])
