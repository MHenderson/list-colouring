import networkx as nx

import listcolouring
from listcolouring import greedy_list_total_colouring

def test_greedy_list_total_colouring():
    G = nx.complete_graph(3)
    permissible_dict_node = {0: [0, 1], 1: [1, 2], 2: [2, 4]}
    nx.set_node_attributes(G, permissible_dict_node, "permissible")
    nx.set_node_attributes(G, None, "colour")
    nx.set_edge_attributes(G, [1, 2, 3], "permissible")
    nx.set_edge_attributes(G, 2, "colour")
    G = greedy_list_total_colouring(G)
    assert G.nodes[0]["colour"] == 0
    assert G.nodes[1]["colour"] == 2
    assert G.nodes[2]["colour"] == 4
