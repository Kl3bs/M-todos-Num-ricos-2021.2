from sympy import *
from sympy.plotting import plot


def solveFunction(expression, a, b, N):

    x, y = symbols('x y')
    res = sympify(expression)
    res = res.subs(x, a)
    # plot(sympify(expression), (x, a, b), line_color='red')
    plot(4, (x, a, b))

    return res


solveFunction("2*x+5", -5, 5, [1, 2, 3, 4, 5])
