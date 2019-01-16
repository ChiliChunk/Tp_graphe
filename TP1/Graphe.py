from TP1.Sommet import Sommet

class Graphe:

    def __init__(self,nbSommet):
        self.sommets = []
        for i in range (nbSommet): #nom Sommet = index dans la liste de sommet
            self.sommets.append(Sommet(i))

    def addArc (self , depart , arrivee):
        depart.suivants.append(arrivee)
        arrivee.precedents.append(depart)

    def addArrete(self,sommet1 , sommet2):
        sommet1.suivants.append(sommet2)
        sommet1.precedents.append(sommet2)
        sommet2.precedents.append(sommet1)
        sommet2.suivants.append(sommet1)

    def getSommet (self , index):
        return self.sommets[index]

    def __str__(self):
        result = ""
        for sommet in self.sommets:
            result += f"{sommet.__str__()}\n"
        return result
