#paul

import networkx as nx
import matplotlib.pyplot as plt

def path_analyse(G, weighted=False):
    weights = G.weight if weighted else None
    iter = dict(nx.shortest_path_length(G), weight=weights)
    plot_distrib(iter, G)




def plot_distrib(iter, G):
    paths = []
    print(G.nodes)
    for i in G.nodes :
        for j in G.nodes :
            if i != j :
                try :
                    paths.append(iter[i][j])
                except:
                    print("no path between " + str(i) + " and " + str(j) + "\n")
    plt.hist(paths)
    plt.xlabel("Taille du plus court chemin")
    plt.ylabel("Nombre de chemins")
    plt.show()