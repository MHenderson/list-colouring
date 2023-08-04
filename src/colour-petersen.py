import random

import networkx as nx

G = nx.petersen_graph()

# create a global list of colours
colours = range(0, 10)

# assign a random subset of colours to the list of permissible colours for every edge
for u, v, permissible in G.edges.data("permissible"):
    G[u][v]["permissible"] = random.sample(colours, 3)

# assign a random colour to every edge
for u, v, colour in G.edges.data("colour"):
    G[u][v]["colour"] = random.choice(colours)

# iterate through nodes and neighbours printing permissible lists and colours
for n, nbrs in G.adj.items():
   for nbr, eattr in nbrs.items():
       perm = eattr['permissible']
       col = eattr['colour']
       print(f"({n}, {nbr}, {perm}, {col})")
