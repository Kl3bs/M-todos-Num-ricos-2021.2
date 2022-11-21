from sympy import *
from sympy.plotting import plot


def solveFunction(expression, a):
    x = symbols('x')
    res = sympify(expression)
    res = res.subs(x, a)
    plot(2*x*5, line_color='red')
    return res


solveFunction("2*x+5", 1)
