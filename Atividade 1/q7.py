
def f(x):
    y = x**3 - 4*x**2 - 10
    return y

def d(x):
    h = 0000000.1
    return ((f(x + h) - (f(x)))/h)


def newton(x0, tol,iterations):
    x = 0
    i = 0
    while abs(f(x0)) > tol:
        x = x0 - f(x0)/d(x0)
        x0 = x
        i = i  + 1
        print(f(x0))
        if (i >= iterations):
            print("Could not find any root")
            break
        
    if i < iterations:
        print("\n\nRoot: %f\nIterations: %d\nf(%f) = %g \n\n" %(x0,i,x0,f(x0)))

newton(1,0000000.1, 20)

print(f(4.495629))

#Errado, precisa revisar o codigo