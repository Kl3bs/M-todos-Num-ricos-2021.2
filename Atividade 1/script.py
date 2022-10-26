import numpy as np
import matplotlib.pyplot as plt

def f(x):
    y = x**3 + 4*x**2 - 10
    return y

def fixedPoint(p0, tol, max_iterations):
    i = 1
    while i <= max_iterations:
        p = f(p0)
        if abs(p - p0) < tol:
            print("Result: ",p)
            break
    i = i + 1
    p0 = p
        
 
fixedPoint(1, 0000.1, 100)

