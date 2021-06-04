import numpy as np

#### 1
def iteration_GJ(matrix,r,s):
    
    pivot = matrix[r,s]
    m = len(matrix)
    n = len(matrix[0])
    for i in range(n) :
        matrix[r,i] = matrix[r,i]/pivot
    for i in range(m) :
        if i != r :
            ais= matrix[i,s]
            for j in range(n) :
                matrix[i,j] = matrix[i,j] - ais*matrix[r,j]
    return matrix


#### 2 matrice inverse
def matrice_inverse(A) : 
    return np.linalg.inv(A)

#### 3 linear system

def linear_system(A,B):

    A = np.array(A)
    print(A)
    B = np.array(B)
    X = np.linalg.inv(A).dot(B)

    print(X)

#### 4_1
print("\n ########## 4_1 \n")
A = [[2, 1, 4], [3, 2, 1], [1, 3, 3]]
B = [16, 10, 16]
linear_system(A,B)

#### 4_2 

print("\n ########## 4_2_B \n")
A = [[2, 1], [3, 1]]
print(matrice_inverse(A))

print("\n ########## 4_2_A \n")

A = [[2, -1, 0], [-1, 2, -1], [0, -1, 2]]
print(matrice_inverse(A))

#### 4_3
print("\n ########## 4_3 \n")
 
A = [[2, -1, 0], [-1, 2, -1], [0, -1, 2]]
B = [10, -4, 2]
B = np.array([10, -4, 2])
x = np.true_divide(A,B)
print(x)

### 4_4
print("\n ########## 4_4_A \n")

w1 = matrice_inverse(A).dot(A)
w2 = matrice_inverse(A).dot(A)

print(w1)
print("\n ########## 4_4_B \n")

print(w2)






