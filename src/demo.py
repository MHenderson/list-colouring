import networkx as nx

G = nx.petersen_graph()

d = nx.coloring.greedy_color(G, strategy="largest_first")

print(G.nodes)
print(G.edges)

G[0][1]["colour"] = 4

print(G[0][1])
print(G[0])

print(d)

G[0][1]["permissible"] = {1, 2, 3}
print(G[0][1])

print(G[0][1]["colour"] in G[0][1]["permissible"])

GL = nx.line_graph(G)

print(GL)

print(nx.inverse_line_graph(GL))

print(GL.nodes)
print(GL.edges)