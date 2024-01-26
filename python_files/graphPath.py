#paul

import networkx as nx
import matplotlib.pyplot as plt

def path_analyse(G, weighted=False):
    iter = dict(nx.shortest_path_length(G, weight = "weight"))
    plot_distrib(iter, G)




def plot_distrib(iter, G):
    paths = []
    #(G.nodes)
    for i in iter:
        for j in iter[i]:
            #print(iter[i][j])
            paths.append(iter[i][j])
    plt.hist(paths)
    plt.xlabel("Taille du plus court chemin")
    plt.ylabel("Nombre de chemins")
    plt.show()