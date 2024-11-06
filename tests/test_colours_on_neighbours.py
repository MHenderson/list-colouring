import networkx as nx

import listcolouring
from listcolouring import colours_on_neighbours

def test_colours_on_neighbours():
    G = nx.complete_graph(3)
    node_colours_dict = {0: 3, 1: 2, 2:1}
    nx.set_node_attributes(G, node_colours_dict, "colour")
    assert colours_on_neighbours(G, 0) == set([2, 1])
    assert colours_on_neighbours(G, 1) == set([3, 1])
    assert colours_on_neighbours(G, 2) == set([3, 2])

