#youssef
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

def calcul_degre_degre_clustering(G):

    # Degré moyen
    dict_degre = dict(G.degree())
    list_degre = list(dict_degre.values())
    degree_moyen = np.mean(list_degre)
    print("Degré moyen : {}".format(degree_moyen))

    # Distribution du degré
    # La liste qui représente l'histogramme des degrés du graphe
    degree_histogram = nx.degree_histogram(G)

    print("Distribution du degré : {}".format(degree_histogram))

    # Moyenne du degré de clustering
    moyenne_degree_clustering = nx.average_clustering(G)
    print("Moyenne du degré de clustering : {}".format(moyenne_degree_clustering))

    # Distribution du degré de clustering
    clustering_coefficients = nx.clustering(G)
    dict_degre_clustering = clustering_coefficients.values()
    list_degre_clustering = list(dict_degre_clustering)
    print("Distribution du degré de clustering : {}".format(list_degre_clustering))


def draw_degree_and_clustering_distributions(G):
    
    # Distribution du degré
    dict_degre = dict(G.degree())
    list_degre = list(dict_degre.values())
    degree_histogram = nx.degree_histogram(G)

    # Tracé de la distribution du degré
    plt.figure(figsize=(5, 5))
    plt.bar(range(len(degree_histogram)), degree_histogram, color='red', alpha=0.6)
    plt.title('Distribution des Degrés')
    plt.xlabel('Degré')
    plt.ylabel('Fréquence')
    plt.show()

    # Distribution du degré de clustering
    clustering_coefficients = nx.clustering(G)
    list_degre_clustering = list(clustering_coefficients.values())

    # Tracé de la distribution du degré de clustering
    plt.figure(figsize=(5, 5))
    plt.hist(list_degre_clustering, bins='auto', color='blue', alpha=0.6, edgecolor='black')
    plt.title('Distribution du Degré de Clustering')
    plt.xlabel('Degré de Clustering')
    plt.ylabel('Fréquence')
    plt.show()
