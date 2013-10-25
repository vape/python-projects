# The graph in this drawing: http://en.wikipedia.org/wiki/File:Dijkstra_Animation.gif
graph = {
    'A': [('B', 7), ('C', 9), ('F', 14)],
    'B': [('A', 7), ('C', 10), ('D', 15)],
    'C': [('A', 9), ('B', 10), ('D', 11), ('F', 2)],
    'D': [('B', 15), ('C', 11), ('E', 6)],
    'E': [('D', 6), ('F', 9)],
    'F': [('A', 14), ('C', 2), ('E', 9)]
}


def get_unvisited_nodes_from(node, visited=[]):
    return [n for n in graph[node] if n[0] not in visited]


def find_shortest_path(node, path=[], total_cost=0):
    if len(path) == len(graph):
        return path, total_cost

    unvisited_nodes = get_unvisited_nodes_from(node, path)
    nodes, costs = list(zip(*unvisited_nodes))
    next_node = nodes[costs.index(min(costs))]
    path.append(next_node)
    total_cost += min(costs)
    return find_shortest_path(next_node, path, total_cost)


def main():
    #print(get_unvisited_nodes_from('A', ['B']))
    print(find_shortest_path('A', ['A']))


if __name__ == '__main__':
    main()