import NetworkX as nx
import matplotlib.pyplot as plt
import numpy as np

import openGraph as og
import graphDeg as gd
import graphClique.py as gc
import graphPath.py as gp

G = og.graphFromCSV(og.FILES[0],distance_limit=40000)
print("import du graph finis...")
og.plotGraph(G)