class Sommet:

    def __init__(self , nom):
        self.nom = nom
        self.couleur = None
        self.suivants = []
        self.precedents = []

    def __str__(self):
        listSuivant = []
        for suivant in self.suivants:
            listSuivant.append(suivant.nom)
        listPrecedent = []
        for precedent  in self.precedents:
            listPrecedent.append(precedent.nom)
        return f"{self.nom} : {self.couleur} , SUIV : {listSuivant} , PREC : {listPrecedent}"

    def toStringNonOriente(self):
        listSuivant = []
        for suivant in self.suivants:
            listSuivant.append(suivant.nom)
        return f"{self.nom} : {self.couleur} , VOISINS : {listSuivant}"

    @property
    def degres(self):
        return len(self.suivants) + len(self.precedents)

    @property
    def voisins(self):
        return list(set(self.precedents+self.suivants))