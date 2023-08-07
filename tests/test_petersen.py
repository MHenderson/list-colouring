import networkx as nx
import matplotlib.pyplot as plt

import listcolouring
from listcolouring import list_init, greedy_list_edge_colouring, print_list_edge_colouring

def test():
    G = nx.petersen_graph()
    G = list_init(G, range(0, 10), 3, 0)
    G = greedy_list_edge_colouring(G)

def test_draw():
    