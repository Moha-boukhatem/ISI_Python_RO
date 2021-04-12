#from TP1 import *

import numpy as np
matrice = [[20, 10,  5, 5, 1, 0,  0, 0,  30], 
          [20, 10, 15, 5, 0, 1,  0, 0, 480], 
          [ 0,  0,  1, 0, 0, 0, -1, 0,  10],
          [ 0,  0,  0, 1, 0, 0,  0, 1,  10],
          [ 3000,  2000,  1000, 1000, 0, 0,  0, 0,  0]]


def find_maximum(a,last_row,length):
    
    a = a[last_row-1]
    
    max = 0
    
    for i in range(0,length):
        
        if a[i] > 0 :
            if  max < a[i] : 
                max = a[i]
                position = i

    return position

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

def find_pivot(matrix,position,length_row,length): 
     
    for i in range(length_row):


        print
def simplex(m):

    
    m = np.array(m)
    a = len(matrice)
    b = len(matrice[0])

    position = find_maximum(m,a,b)
    r,s = find_pivot(matrice,position,a,b)
    print(iteration_GJ(matrice,r,s))

    
simplex(matrice)


