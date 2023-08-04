import random

import networkx as nx

G = nx.petersen_graph()

print(G.edges)

print(list(nx.edge_dfs(G, source=0)))

for u, v, colour in G.edges.data("colour"):
    G[u][v]["colour"] = random.randint(0, 3)

print(G.edges)
print(G.edges.data("colour"))

for n, nbrs in G.adj.items():
   for nbr, eattr in nbrs.items():
       wt = eattr['colour']
       print(f"({n}, {nbr}, {wt})")

def used_at(G, v):
    return(True)

print(used_at(G, 0))