import numpy as np


def isVStochastic(nb) : 
    
    vector = []

    print("##### elements like '0.3','0.2','0.5' ")

    for i in range(nb):
        element = float(input("element : "))
        vector.append(element)

    vector = np.array(vector)
    somme = np.sum(vector)
    
    if somme == 1 or somme == 0.9999999999999999 : 
        return (True,vector)    
    else :
       return (False,vector)


def isMStochastic():
    
    n = int(input("the matrix dimension : "))
    listValidation = []
    matrix = []



    for i in range(n) : 
        val,vector = isVStochastic(n)
        listValidation.append(val)
        matrix.append(vector)

    
    matrix = np.array(matrix)

    if False in listValidation :
        return (False,matrix)
    else : 
        return (True,matrix)


def CalculMartix():

    neg = False
    nb = int(input("type M : "))
    val,matrix = isMStochastic ()
    
    if val:
        for rowPosition,row in enumerate(matrix) : 
            for colPosition,col in enumerate(row):
                if col < 0 :
                    print("negative value in [",rowPosition,",",colPosition,"]")
                    neg  = True


        if  neg == False :
            print("\n Matrix : \n")
            print(matrix)
            print("\nMatrix ^",nb," : \n")
            print(np.power(matrix,nb))

    else : 
        print(matrix," isn't Stochastic")


def switch_def ():
    
    while True : 

        print('''
    1 - Vector is Stochastic ()
    2 - Matrix is Stochastic ()
    3 - Calcul Martix ()
    4 - Exit''')

        choice = int(input("type the Question : "))

        if choice == 1:
            nb = int(input("Nb of vector elements : "))
            val,vector = isVStochastic(nb)

            if val:
                print(vector," is Stochastic") 
            else :
                print(vector," isn't Stochastic") 


        elif choice == 2:
            val,matrix = isMStochastic()

            if val:
                print(matrix," is Stochastic") 
            else :
                print(matrix," isn't Stochastic") 
        
        elif choice == 3:

            CalculMartix()


        elif choice == 4 : 
            break
        else : 
            print("invalid input")
            

if __name__ == "__main__" :
    
    switch_def ()