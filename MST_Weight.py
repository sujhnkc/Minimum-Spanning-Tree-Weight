# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 21:11:26 2020

@author: Sujoy HNKC
"""


import matplotlib.pyplot as plt
import networkx as nx
from networkx.utils import pairwise, not_implemented_for



G = nx.read_graphml('Sample_Graph.graphml')

mst=nx.minimum_spanning_edges(G,data=True)
edgelist=list(mst)

print(edgelist)


total_w=0.0
j=0
for i in edgelist:
    total_w=total_w + i[2].get('weight')
    print(i[2].get('weight'))
    j=j+1
    
    
print('Total weight:')
print(total_w)
print('Total Edges:')
print(j)