from sympy import *
from sympy.plotting import plot


def solveFunction(expression, a, b, N):

    x, y = symbols('x y')
    res = sympify(expression)

    plot(sympify(expression), xlim=(a, b), ylim=(a, b), line_color='red',
         markers=[{'args': [[1, 2, 3], [1, 2, 3], "o"]}])

    return res


print(solveFunction("x**2+2*x+5", -5, 5, 3))
