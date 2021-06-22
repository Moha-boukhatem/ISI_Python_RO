import numpy as np


def isVStochastic(vector) : 
    
    vector = np.array(vector)
    somme = np.sum(vector)
    
    if somme == 1 : 
        return True    
    else :
       return False


def isMStochastic(matrix):
    
    liste = []
    
    for row in matrix : 
        liste.append(isVStochastic(row))

    if False in liste :
        return False
    else : 
        return True


def CalculMartix(matrix):

    if isMStochastic(matrix):
        for row in matrix : 
            for col in row:
                if col < 0 :
                    return False

        return np.dot(matrix,matrix)
    return False


if __name__ == "__main__" :
    
    vector = [1/5,2/10,3/5]

    matrix =  [[3/5,1/5,2/10],
               [2/10,1/5,3/5],
               [1/5,6/5,-2/5]]

    rep = isVStochastic(vector)
    
    print(isVStochastic(vector))
    print(isMStochastic(matrix))
    print(CalculMartix(matrix))