import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

import openGraph as og
import graphDeg as gd
import graphClique as gc
import graphPath as gp

G = og.graphFromCSV(og.FILES[0],distance_limit=40000)
print("import du graph finis...")
og.plotGraph(G)
gp.path_analyse(G, True)