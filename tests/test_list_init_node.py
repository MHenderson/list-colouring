import networkx as nx

import listcolouring
from listcolouring import list_init_node

def test_list_init_node():
    G = nx.petersen_graph()
    G = list_init_node(G, range(0, 10), 3, 0)
    assert G.nodes[0]['colour'] is None
    assert len(G.nodes[0]['permissible']) == 3
