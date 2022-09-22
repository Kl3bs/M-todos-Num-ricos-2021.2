import math

def absolute_error(p, p_star):
    return abs(p-p_star)

def relative_error(p,p_star):
    return absolute_error(p,p_star)/abs(p)

 
def get_max_interval(p, index):
    max_error = p * math.pow(10,-3)
    
    if relative_error(p,p+index) > max_error:
        print("For p =" ,p, "p* must be between", p,"and",p + index - 1, '\nMax error =', max_error , "\nRelative error with p* =", p + index - 1 , ':' ,relative_error(p, p + index - 1), '\n' )
        return

    
    return get_max_interval(p, index + 1)


get_max_interval(150,0)
get_max_interval(900, 0)
# get_max_interval(1500, 0)
get_max_interval(90, 0)

 