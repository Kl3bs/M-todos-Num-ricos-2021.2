import numpy as np
from sympy import *


def solveFunction(expression, a):
    x = symbols('x')
    res = sympify(expression)
    res = res.subs(x, a)
    return res


def firstDerivative(function, points, h):
    res = []
    for i in range(len(points)):
        d_dx = (solveFunction(function, points[i] + h) -
                solveFunction(function, points[i]-h)) * (1/(2*h))
        res.append(d_dx)
    return res


def secondDerivative(function, points, h):
    res = []
    for i in range(len(points)):
        d_dx = ((solveFunction(function, points[i] - h) - 2*(solveFunction(function,
                points[i])) + solveFunction(function, points[i]+h))) * (1/(h**2))
        res.append(d_dx)
    return res


def plotDerivative(function, points, n):
    x = symbols('x')

    if n == 1:

        graph = plot(sympify(function),  diff(sympify(function), x),  legend=True, xlabel='x', ylabel='f(x)',  title="First derivative",
                     markers=[{'args': [points, "o"]}])
    else:
        graph = plot(diff(sympify(function), x), diff(sympify(function), x, 2),  legend=True, xlabel='x', ylabel='f(x)',  title="Second derivative",
                     markers=[{'args': [points, "o"]}])

    graph[0].line_color = 'b'
    graph[1].line_color = 'g'


# print(firstDerivative("x**2+3*x+3", [0, 1, 2, 3, 4], 0.1))
# print(secondDerivative("x**2+3*x+3", [0, 1, 2, 3, 4], 0.1))
# * (1/(h**2))
function2 = "x**3-x"
p = secondDerivative(function2, [0, 1, 2, 3, 4], 0.1)
plotSecondDerivative(function2, p)
