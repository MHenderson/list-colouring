import networkx as nx

import listcolouring
from listcolouring import greedy_list_node_colouring

def test_greedy_list_node_colouring():
  G = nx.complete_graph(3)
  permissible_dict = {0: [0, 1], 1: [1, 2], 2: [2, 3]}
  nx.set_node_attributes(G, permissible_dict, "permissible")
  nx.set_node_attributes(G, None, "colour")
  G = greedy_list_node_colouring(G)
  assert G.nodes[0]["colour"] == 0
  assert G.nodes[1]["colour"] == 1
  assert G.nodes[2]["colour"] == 2
