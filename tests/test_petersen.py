import networkx as nx
import matplotlib.pyplot as plt

import listcolouring
from listcolouring import list_init, greedy_list_edge_colouring, print_list_edge_colouring

def test():
    G = nx.petersen_graph()
    G = list_init(G, range(0, 10), 3, 0)
    G = greedy_list_edge_colouring(G)

def test_draw():
    G = nx.petersen_graph()
    G = list_init(G, range(0, 10), 3, 0)
    G = greedy_list_edge_colouring(G)
    options = {'with_labels': True, 'node_color': "white"}
    # this won't work if there is an uncoloured edge (i.e. None)
    colors = nx.get_edge_attributes(G,'colour').values()
    nx.draw_shell(G, nlist = [range(5, 10), range(5)], edge_color = colors, **options)
    #plt.savefig("img/petersen-shell.png", format = "PNG")