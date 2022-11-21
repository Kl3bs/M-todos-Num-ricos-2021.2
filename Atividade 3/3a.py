from sympy import *


def solveFunction(expression, a):
    x = symbols('x')
    res = sympify(expression)
    res = res.subs(x, a)
    return res


solveFunction("2*x+5", 1)
