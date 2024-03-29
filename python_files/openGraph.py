import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import csv 
import scipy

FILES = ["../topology_low.csv","../topology_avg.csv","../topology_high.csv"]

def graphFromCSV (filename, delimiter = ',', distance_limit = 20000, valuated = True) :
    G = nx.Graph()
    positions = []
    with open(filename, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=delimiter, quotechar='|')
        print(next(spamreader)) # skip first line

        for row in spamreader:
            
            actual_pos = (float(row[1]),float(row[2]),float(row[3]))
            G.add_node(int(row[0]), pos =actual_pos)
            #on calcul maintenant toutes les distances pour les ajouter au graphe
            for i in range(len(positions)) :
                dist = np.linalg.norm(np.array(actual_pos) - np.array(positions[i]))

                if dist < distance_limit or distance_limit == -1:
                    if valuated :
                        G.add_edge(int(row[0]), int(i), weight=dist)
                    else : 
                        G.add_edge(int(row[0]), int(i), weight=1)
        
            positions.append((float(row[1]),float(row[2]),float(row[3])))
        
    return G

        
def plotGraph(G,title = "Graph",colored = [], degree_coloration = True) :
    pos = nx.get_node_attributes(G,"pos")
    edges_xyz = np.array([np.array([pos[u],pos[v]]) for u, v in G.edges()])
    nodes_xyz = np.array([pos[u] for u in G.nodes()])

    colored_xyz = np.array([pos[u] for u in G.subgraph(colored).nodes()])
    colored_edges_xyz = np.array([np.array([pos[u],pos[v]]) for u, v in G.subgraph(colored).edges()])

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')


    if degree_coloration :
        degrees= nx.degree(G)
        colors = [degrees[node] for node in G.nodes()]
        ax.scatter(*nodes_xyz.T, s=100, c=colors,ec ="w")
    else :
        ax.scatter(*nodes_xyz.T, s=100,ec ="w")
    
    for vizedge in edges_xyz :
        ax.plot(*vizedge.T, color='b', alpha=0.2)

    if colored != [] :
        ax.scatter(*colored_xyz.T, s=100, c="r",ec ="w")
        for vizedge in colored_edges_xyz :
            ax.plot(*vizedge.T, color='r', alpha=1)
    
    
    def _format_axes(ax) :
        ax.grid(False)
        for dim in (ax.xaxis, ax.yaxis, ax.zaxis):
            dim.set_ticks([])
    
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")

    _format_axes(ax)
    fig.tight_layout()
    plt.title(title)

    plt.show()


def printGraph(G) :
    for n in G.nodes() :
        print("="*20)
        print(n)
        
    print(nx.get_node_attributes(G,"pos"))

if __name__ == "__main__" :
    print("ok bb")
    G = graphFromCSV(FILES[0],distance_limit=40000)
    print("import du graph finis...")
    plotGraph(G)

