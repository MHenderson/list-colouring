import random

import networkx as nx
import matplotlib.pyplot as plt

random.seed(0)

G = nx.petersen_graph()

# create a global list of colours
colours = range(0, 10)

# assign a random subset of colours to the list of permissible colours for every edge
for u, v, permissible in G.edges.data("permissible"):
    G[u][v]["permissible"] = random.sample(colours, 3)

# initialise the colour of every edge to None
for u, v, colour in G.edges.data("colour"):
    G[u][v]["colour"] = None

# colours_incident_with
def colours_incident_with(G, u):
    return(set([G[u][v]["colour"] for v in nx.neighbors(G, u)]))

# first_permissible_or_none
# given G, u and v this function returns the first element of A if A is not empty otherwise None
# A is P minus (X union Y)
# where X is the list of colours on edges incident with u
#       Y is the list of colours on edges incident with v
#       P is the list of permissible colours for edge uv
def first_permissible_or_none(G, u, v):
    X = colours_incident_with(G, u)
    Y = colours_incident_with(G, v)
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

options = {
 'with_labels': True,
 'node_color': "white"
}

# this won't work if there is an uncoloured edge (i.e. None)
colors = nx.get_edge_attributes(G,'colour').values()

nx.draw_shell(G, nlist = [range(5, 10), range(5)], edge_color = colors, **options)
plt.savefig("img/petersen-shell.png", format = "PNG")