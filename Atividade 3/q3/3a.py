from sympy import *


def solveFunction(expression, a):
    x = symbols('x')
    res = sympify(expression)
    res = res.subs(x, a)
    return res


print(solveFunction("x*e**x", 2))
