import random

import networkx as nx

G = nx.petersen_graph()

# create a global list of colours
colours = range(0, 10)

# assign a random subset of colours to the list of permissible colours for every edge
for u, v, permissible in G.edges.data("permissible"):
    G[u][v]["permissible"] = random.sample(colours, 3)

# colours_incident_with
def colours_incident_with(G, u):
    return([1, 2, 3, 4, 5])

# first_permissible_or_none
# given G, u and v this function returns the first element of A if A is not empty otherwise None
# A is P minus (X union Y)
# where X is the list of colours on edges incident with u
#       Y is the list of colours on edges incident with v
#       P is the list of permissible colours for edge uv
def first_permissible_or_none(G, u, v):
    X = set(colours_incident_with(G, u))
    Y = set(colours_incident_with(G, v))
    P = set(G[u][v]["permissible"])
    choices = P - X.union(Y)
    if(len(choices) > 0):
        choice = list(choices)[0]
    else:
        choice = None
    return(choice)

# assign the first permissible colour to every edge (or None if all permissible colours already used on incident edges)
for u, v, colour in G.edges.data("colour"):
    G[u][v]["colour"] = first_permissible_or_none(G, u, v) # random.choice(colours)

# iterate through nodes and neighbours printing permissible lists and colours
for n, nbrs in G.adj.items():
   for nbr, eattr in nbrs.items():
       perm = eattr['permissible']
       col = eattr['colour']
       print(f"({n}, {nbr}, {perm}, {col})")

print(colours_incident_with(G, 4))

print(nx.edges(G, 3))

print([v for v in nx.neighbors(G, 3)])