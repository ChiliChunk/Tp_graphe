from TP1.Sommet import Sommet
from TP1.Graphe import Graphe

g = Graphe(5 , False)

g.addArrete(g.getSommet(2),g.getSommet(4))
g.addArrete(g.getSommet(1),g.getSommet(2))
g.addArrete(g.getSommet(3),g.getSommet(4))
g.addArrete(g.getSommet(0),g.getSommet(1))
g.welshPowell()
print(g)