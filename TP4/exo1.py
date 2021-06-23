from random import choice


class dice:
    def __init__(self):
        self.diceNumbers = [1,2,3,4,5,6]


class coin : 
    def __init__(self):
        self.coinList = ["Face","Pile"]


def Question1():
    
    nb = choice(dice().diceNumbers)

    print("Le chiffre : ",nb)


def Question2():
    
    n = int(input("Donner nb du lancement : "))
    appearance = []
    
    for i in range(n):
        appearance.append(choice(dice().diceNumbers))
    print("Liste d'apparitions : ",appearance)


def appearance(object):
    
    n = int(input("Donner nb du lancement : "))
    appearance = []
    
    for i in range(n):
        appearance.append(choice(object))
    return appearance


def Question3():

    liste = appearance(dice().diceNumbers)
    print("liste : ",liste)
    print("Nb d'apparitions du 6  : ",liste.count(6))


def Question4():
    
    Q4_Liste = []
    
    while True :
        
        nb = choice(dice().diceNumbers)
        Q4_Liste.append(nb)

        if nb == 6 :
            break
    print("Liste d'apparitions : ",Q4_Liste)
    print("Nb de lancements pour obtenir 6 : ",len(Q4_Liste))


def Question5():
    print(appearance(coin().coinList))

def switch_def ():
    
    while True : 
        print('''
    1 - Question1()
    2 - Question2()
    3 - Question3()
    4 - Question4()
    5 - Question5()
    6 - Exit''')

        choice = int(input("type the Question : "))

        if choice == 1:
            Question1()

        elif choice == 2:
            Question2()
        
        elif choice == 3:
            Question3()

        elif choice == 4:
            Question4()

        elif choice == 5:
            Question5()
        
        elif choice == 6 : 
            break
        else : 
            print("invalid input")
            
      
      
if __name__ == '__main__':

    
    

    switch_def()