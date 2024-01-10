#céleste
import networkx as nx
import matplotlib.pyplot as plt
import openGraph as og

#algorithme qui renvoie l'ordre et le nombre de clique de G
# se repose sur nx.find_cliques(G)
def cliques(G) :
    clq = []
    s = 0
    for clique in nx.find_cliques(G) :
        if len(clique) > 2 :
            clq.append(len(clique))
            s+= 1
    return s,clq

def connectedComponents(G) :
    ccs = []
    s = 0
    for cc in nx.connected_components(G) :
        if len(cc) > 2 :
            ccs.append(len(cc))
            s+= 1
    return s,ccs

def histcliques (G) :
    s,clq = cliques(G)
    print(clq)
    plt.hist(clq, bins = 20)
    plt.xlabel("Taille des cliques")
    plt.ylabel("Nombre de cliques")
    plt.show()
    return s,clq

def histconnnectedComponents (G) :
    s,ccs = connectedComponents(G)
    print(ccs)
    plt.hist(ccs, bins = 20)
    plt.xlabel("Taille des composantes connexes")
    plt.ylabel("Nombre de composantes connexes")
    plt.show()
    return s,ccs

def bigest_clique (G) : 
    s,clq = cliques(G)
    clq = []
    s = 0
    for clique in nx.find_cliques(G) :
        if len(clique) > 2 :
            clq.append(clique)
            s+= 1
    return max(clq, key=len)

def bigest_connectedComponents (G) : 
    s,ccs = connectedComponents(G)
    ccs = []
    s = 0
    for cc in nx.connected_components(G) :
        if len(cc) > 2 :
            ccs.append(cc)
            s+= 1
    return max(ccs, key=len)

if __name__ == "__main__" :
    G = og.graphFromCSV(og.FILES[0],distance_limit=20000)
    print("import du graph finis...")
    histconnnectedComponents(G)