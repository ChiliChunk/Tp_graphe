from TP1.Sommet import Sommet

class Graphe:

    def __init__(self,nbSommet , oriente):
        self.sommets = []
        self.oriente = oriente
        for i in range (nbSommet): #nom Sommet = index dans la liste de sommet
            self.sommets.append(Sommet(i))

    def addArc (self , depart , arrivee , poid):
        if not self.oriente:
            self.addArrete(depart,arrivee , poid)
        else:
            depart.suivants.append((arrivee , poid))
            arrivee.precedents.append((depart , poid))

    def addArrete(self,sommet1 , sommet2 , poid):
        sommet1.suivants.append((sommet2, poid))
        sommet1.precedents.append((sommet2 , poid))
        sommet2.precedents.append((sommet1 , poid))
        sommet2.suivants.append((sommet1 , poid))

    def getSommet (self , index):
        return self.sommets[index]

    def __str__(self):
        result = ""
        if self.oriente:
            for sommet in self.sommets:
                result += f"{sommet.__str__()}\n"
        else:
            for sommet in self.sommets:
                result += f"{sommet.toStringNonOriente()}\n"
        return result

    def welshPowell(self):
        listCouleur=['RED','GREEN','BLUE','BLACK','WHITE','PURPLE','BROWN','YELLOW','PINK']
        cursorUsed = 0
        self.trierDecroissant()
        for sommet in self.sommets:
            if sommet.couleur == None:
                sommet.couleur = listCouleur[cursorUsed]
                for sommet2 in self.sommets:
                    if not sommet2 in sommet.voisins:
                        sommet2.couleur = listCouleur[cursorUsed]
                cursorUsed += 1

    def trierDecroissant(self):
        for i in range (len(self.sommets)):
            for j in range (len(self.sommets)-1):
                if self.sommets[j].degres < self.sommets[j+1].degres:
                    temp = self.sommets[j]
                    self.sommets[j] = self.sommets[j+1]
                    self.sommets[j+1] = temp

