import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

import openGraph as og
import graphDeg as gd
import graphClique as gc
import graphPath as gp

distance_limite = 40000
IDX = 1

G = og.graphFromCSV(og.FILES[IDX],distance_limit=distance_limite,valuated=True)
print("import du graph finis...")

# ----------------plus courts chemins----------

og.plotGraph(G, "graph n°"+str(IDX)+", distance limite : "+str(distance_limite))
gp.path_analyse(G, True)

# -----------------cliques et composantes connexes------------

G = og.graphFromCSV(og.FILES[0],distance_limit=distance_limite)
#on plot l'histograme des cliques : 
gc.histcliques(G)
# on obtient comme plus grande clique : 
clique = gc.bigest_clique(G)
og.plotGraph(G, "plus grande clique", clique)

#on plot l'histograme des composantes connexes :
gc.histconnnectedComponents(G)
# on obtient comme plus grande composante connexe :
cc = gc.bigest_connectedComponents(G)
og.plotGraph(G, "plus grande composante connexe",cc)

# -----------------degrés------------
gd.calcul_degre_degre_clustering(G) 
