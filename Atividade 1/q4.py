import math
import q2 as q2
 
def truncate(number, decimal_places):
    aux = str(number).split('.')
    return float(aux[0] + '.'+  aux[1][:decimal_places])


def round_number(number, decimal_places):
    return round(number, decimal_places)


def result(exact_value, approximation, digits):
    print("Exact value (%d digits):" % digits, exact_value)
    print("Absolute error: ", q2.absolute_error(exact_value, approximation))
    print("Relative error: ", q2.relative_error(exact_value, approximation))
    print('\n')
 
def f(x):
    y = x**2/3 - (123/4) * x + 1/6 
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
        
        if (i >= iterations):
            print("Could not find any root")
            break
        
    if i < iterations:
        
        return x0
    
def summation():
    res = 0
    i = 1
    for i in ( n+1 for n in range(9)): # i starts at 1
        res =  res + (-1)**i*5**i/math.factorial(i)
    return res

#a) 
exact_a = -10 * math.pi + 6 * math.e - 0.327
a_3 = truncate(exact_a, 3)  #truncamento com 3 digitos
a_4 = truncate(exact_a, 4)  #truncamento com 4 digitos

# result(exact_a, a_3, 3)
# result(exact_a, a_4, 4)


#b)

exact_b = newton(0.1,1, 150)
b_3 = truncate(exact_b, 3)  #truncamento com 3 digitos
b_4 = truncate(exact_b, 4)  #truncamento com 4 digitos


#c)

exact_c = math.e**-5
c_3 = truncate(exact_c, 3)
c_4 = truncate(exact_c, 4)
result(exact_c, c_3, 3)
 