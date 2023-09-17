import networkx as nx

class GraphCreator:
    def __init__(self, nodes: int, edges: int) -> None:
        self.nodes = nodes
        self.edges = edges

    def generate_connected_random_graph(self) -> tuple:
        while True:
            graph = nx.gnm_random_graph(self.nodes, self.edges)
            if nx.is_connected(graph):
                return (graph, nx.spring_layout(graph))