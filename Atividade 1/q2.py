#Implemente algoritmos para calcular o erro absoluto e o erro relativo das aproximações de p por p* ;

#Erro absoluto = |p-p*|
#Erro relativo = |p-p*| / |p|
#Para p != 0

import math

def absolute_error(p, p_star):
    return abs(p-p_star)

def relative_error(p,p_star):
    return absolute_error(p,p_star)/abs(p)

def generate_result(p,p_star):
    print ("For p =", p , "and p* =", p_star)
    print("Absolute error =", absolute_error(p, p_star))
    print("Relative error =", relative_error(p, p_star))
    print("\n")

#A)
p = math.pi
p_star = 3
#generate_result(p,p_star)


#B)
p = math.sqrt(2)
p_star = 1.414
#generate_result(p,p_star)
 
#C)
p = math.e**10
p_star = 22000
#generate_result(p,p_star)


#D)
p = math.factorial(9)
p_star = (math.sqrt(18*math.pi) * (9/math.e)**9)
#generate_result(p,p_star)
 

 


    