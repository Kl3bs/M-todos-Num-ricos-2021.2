import numpy as np
#https://github.com/smaje99/numerical-methods-udla

def gauss_jordan(A, b, table: list) -> np.array:
 
    n = len(b)
    A_aux = np.copy(A)
    b_aux = np.copy(b)

    for k in range(n):
        
        if np.fabs(A_aux[k, k]) < 1.0e-12:
            for i in range(k + 1, n):
                if np.fabs(A_aux[i, k]) > np.fabs(A_aux[k, k]):
                    A_aux[[k, i]] = A_aux[[i, k]]
                    b_aux[[k, i]] = b_aux[[i, k]]
                    table.append([k, 'Swap', i, None, None])
                    break

         
        pivot = A_aux[k, k]
        A_aux[k, k:] /= pivot
        b_aux[k] /= pivot

        
        for i in range(n):
            if i == k or A_aux[i, k] == 0:
                continue

            factor = A_aux[i, k]
            A_aux[i, k:] -= A_aux[k, k:] * factor
            b_aux[i] -= b_aux[k] * factor

            table.append([k, 'Elimination', i, pivot, factor])

    return b_aux


a1=np.array([[1.0,1.0,2.0],[2.0,-1.0,-1.0],[1.0,-1.0,-1.0]])
b1=np.array([4.0,0.0,-1.0])

print(gauss_jordan(a1,b1, []))