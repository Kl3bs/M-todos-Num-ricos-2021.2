from sympy import *
from sympy.plotting import plot


def solveFunction(expression, a, b, N):

    x, y = symbols('x y')
    res = sympify(expression)
    # res = res.subs(N)
    plot(sympify(expression), (x, a, b), line_color='red')

    return res


print(solveFunction("2*x+5", -5, 5, 3))
