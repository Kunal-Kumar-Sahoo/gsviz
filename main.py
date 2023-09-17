from gsviz import graph_generator, bfs, dfs, visualization


if __name__ == '__main__':
    nodes = int(input('Enter number of nodes: '))
    edges = int(input('Enter number of edges: '))

    graph_generator = graph_generator.GraphCreator(nodes, edges)
    (graph, pos) = graph_generator.generate_connected_random_graph()

    bfs_order = bfs.BFSOrderer().order_bfs(graph, 0)
    dfs_order = dfs.DFSOrderer().order_dfs(graph, 0)

    visualizer = visualization.Visualizer()
    visualizer.visualize_search(graph, pos, bfs_order, 'BFS Visualization')
    visualizer.visualize_search(graph, pos, dfs_order, 'DFS Visualization')