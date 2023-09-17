# Graph Search and Visualization Library

This is a Python3 library for creating random graphs, performing *breadth-first search* and *depth-first search*, and visualizing the search process using NetworkX and Matplotlib.

## Features

- Generate a connected random graph.
- Perform BFS and DFS algorithms.
- Visualize the search process with animated graphs.

## Installation

To install the library, you can use `pip`:
```bash 
pip install gsviz
```

## Usage
Here's how you can use the library in your Python3 script:

```python
from gsviz import graph_generator, bfs, dfs, visualization

graph_generator = graph_generator.GraphCreator(20, 20)
(graph, pos) = graph_generator.generate_connected_random_graph()

bfs_order = bfs.BFSOrderer().order_bfs(graph, 0)
dfs_order = dfs.DFSOrderer().order_dfs(graph, 0)

visualizer = visualization.Visualizer()
visualizer.visualize_search(graph, pos, bfs_order, 'BFS Visualization')
visualizer.visualize_search(graph, pos, dfs_order, 'DFS Visualization')
```

## License

This library is licensed under the MIT License. See the [LICENSE](LICENSE.txt) file for detail.


## Author

- [Kunal Kumar Sahoo](https://github.com/Kunal-Kumar-Sahoo/)


## Contributing 

If you would like to contribute to this library, please open an issue or submit a pull request.


## Acknowledgements

- [NetworkX](https://networkx.org)
- [Matplotlib](https://matplotlib.org/)