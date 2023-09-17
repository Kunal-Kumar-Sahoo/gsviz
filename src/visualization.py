import matplotlib.pyplot as plt
import time
import networkx as nx


class Visualizer:
    def visualize_search(self, graph: nx.Graph, pos: nx.spring_layout, order: list, title: str):
        plt.figure()
        plt.title(title)

        for node in order:
            plt.clf()
            plt.title(title)
            nx.draw(graph, pos, with_labels=True, 
                    node_color=['r' if n == node else 'g' for n in graph.nodes])
            plt.draw()
            plt.pause(0.5)
        plt.show()
        time.sleep(0.5)