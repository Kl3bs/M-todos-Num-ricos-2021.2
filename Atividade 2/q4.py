import q1
import numpy as np
import matplotlib.pyplot as plt


def generateRandomMatrix(n, int_only):
    #n is the matrix size
    #int_only = True returns an integer SPD matrix, False is the default value
    if int_only == True:
        return np.random.randint(10, size=(n, n)) 
    return np.random.rand(n, n)

def generateSPD(n,int_only:bool=False):
    A = generateRandomMatrix(n, int_only)
    A_transpose = np.transpose(A)
    return np.dot(A, A_transpose)    


print("Matrix 1:\n", generateSPD(2), "\n")
print("Matrix 2:\n", generateSPD(3, True), "\n")
print("Matrix 2:\n", generateSPD(15), "\n")

"""Todas as matrizes são positivas e definidas, pois são geradas a partir do produto de uma matriz A pela sua transposta (A = A ̇Aˆt).

**QUESTÃO 4**

A)
"""

def generateRandomVector(n):
    return np.random.rand(n)

x = [10,100,500,1000,1500,2000]
y = []

def getCholeskysTime(n):
  n = n
  time = 0
  for item in range(10):
    A = generateSPD(n)
    B =  generateRandomVector(n)
    time += q1.cholesky(A,B)

  print("  Total time: %s" % time)

  y.append(time/60)
  return time

def getGaussTime(n):
    n = n
    time = 0
    for item in range(10):
        A = generateSPD(n)
        B =  generateRandomVector(n)
        time += q1.gaussElimination(A,B)[1]

    print("  Total time: %s" % time)

    y.append(time/60)
    return time

# getCholeskysTime(10)
# getCholeskysTime(100)
# getCholeskysTime(500)
# getCholeskysTime(1000)
# getCholeskysTime(1500)
# getCholeskysTime(2000)

 
getGaussTime(10)
getGaussTime(100)
getGaussTime(500)
getGaussTime(1000)
getGaussTime(1500)
getGaussTime(2000)

plt.plot(x, y)
plt.show()