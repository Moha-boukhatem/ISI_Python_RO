import numpy as np
m = 5
n = 5
matrix = np.random.randint(1,10,(m,n))
def iteration_GJ(matrix,r,s):
    
    pivot = matrix[r,s]
    for i in range(n) :
        matrix[r,i] = matrix[r,i]/pivot
    for i in range(m) :
        if i != r :
            ais= matrix[i,s]
            for j in range(n) :
                matrix[i,j] = matrix[i,j] - ais*matrix[r,j]
    return matrix
print(matrix)
print(iteration_GJ(matrix,2,3))
k = iteration_GJ(matrix,2,3)
print(np.linalg.inv(k)) 
