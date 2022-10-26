import numpy as np 

def generateRandomMatrix(n, int_only):
    
    #n is the matrix sizes
    #int_only = True returns an integer SPD matrix, False is the default value

    if int_only == True:
        return np.random.randint(10, size=(n, n)) 
    return np.random.rand(n, n)


def generateSPD(n,int_only:bool=False):
    A = generateRandomMatrix(n, int_only)
    A_transpose = np.transpose(A)
    return np.dot(A, A_transpose)    
 

# print("Matrix 1:\n", generateSPD(2), "\n")

# print("Matrix 2:\n", generateSPD(3), "\n")


m = generateSPD(10, True)

with open('res.txt', 'w') as f:
    for item in m:
        f.write(np.array2string(item))
        f.write('\n')