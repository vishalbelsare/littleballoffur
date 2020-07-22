import networkx as nx
import networkit as nk
from littleballoffur import NetworKitBackEnd, NetworkXBackEnd

def test_networkit_backend():

    backend = NetworKitBackEnd()

    graph = nk.generators.WattsStrogatzGenerator(1000, 10, 0.5).generate()

    assert 1000 == backend.get_number_of_nodes(graph)
    assert 10000 == backend.get_number_of_edges(graph)

def test_networkx_backend():

    backend = NetworkXBackEnd()

    graph = nx.watts_strogatz_graph(1000, 10, 0.5)

    assert 1000 == backend.get_number_of_nodes(graph)
    assert 5000 == backend.get_number_of_edges(graph)
