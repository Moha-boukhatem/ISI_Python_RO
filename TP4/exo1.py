from random import choice


class dice:
    def __init__(self):
        self.diceNumbers = [1,2,3,4,5,6]


class coin : 
    def __init__(self):
        self.coinList = ["Face","Pile"]


def Question2(object):
    
    n = int(input("Donner nb du lancement : "))
    appearance = []
    
    for i in range(n):
        appearance.append(choice(object))
    print("Liste d'apparitions : ",appearance)
    return appearance


def Question3():

    nbAppearance = Question2(dice().diceNumbers).count(6)
    print("Nb d'apparitions du 6  : ",nbAppearance)


def Question4():
    
    Q4_Liste = []
    
    while True :
        
        nb = choice(dice().diceNumbers)
        Q4_Liste.append(nb)

        if nb == 6 :
            break
    print("Liste d'apparitions : ",Q4_Liste)
    print("Nb de lancements avant obtenir 6 : ",len(Q4_Liste))


def Question5():
    Question2(coin().coinList)
      
        
if __name__ == '__main__':

    print("####### Q3")
    Question3()
    print("####### Q4")
    Question4()
    print("####### Q5")
    Question5()        
            

