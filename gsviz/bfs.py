import queue
import networkx as nx

class BFSOrderer:
    def __init__(self) -> None:
        self.visited = set()
        self.queue = queue.Queue()
        self.order = list()

    def order_bfs(self, graph: nx.Graph, start_node: int) -> list:
        self.queue.put(start_node)

        while not self.queue.empty():
            vertex = self.queue.get()
            if not vertex in self.visited:
                self.order.append(vertex)
                self.visited.add(vertex)
                for neighbor_node in graph[vertex]:
                    if neighbor_node not in self.visited:
                        self.queue.put(neighbor_node)
        
        return self.order