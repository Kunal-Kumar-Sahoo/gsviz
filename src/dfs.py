import queue
import networkx as nx

class DFSOrderer:
    def __init__(self):
        self.visited = set()

    def order_dfs(self, graph: nx.Graph, start_node: int) -> list:
        order = []

        if start_node not in self.visited:
            order.append(start_node)
            self.visited.add(start_node)
            for neighbor_node in graph[start_node]:
                if neighbor_node not in self.visited:
                    order.extend(self.order_dfs(graph, neighbor_node))
        
        return order
