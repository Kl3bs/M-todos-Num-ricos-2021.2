from sympy import *
from sympy.plotting import plot


def plotFunction(expression, a, b, N):

    arr = []
    x, y = symbols('x y')
    res = sympify(expression)

    for i in range(len(N)):
        arr.append(res.subs(x, N[i]))

    plot(sympify(expression), xlim=(a, b), ylim=(a, b), line_color='green',
         markers=[{'args': [arr, "o"]}])

    return arr


print(plotFunction("x*2.718**x", -20, 20, [0, 1, 2, 3, 4]))
