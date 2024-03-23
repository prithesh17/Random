def aStarAlgo(start_node, stop_node):
    open_set = set([start_node])  # Initialize open set with start node
    closed_set = set()  # Initialize closed set
    g = {}  # Cost from start node to current node
    parents = {}  # Parent nodes for each node

    g[start_node] = 0  # Cost from start node to itself is 0
    parents[start_node] = start_node  # Parent of start node is itself

    # Main A* algorithm loop
    while len(open_set) > 0:
        n = None  # Current node
        # Find the node with the lowest f(n) = g(n) + h(n)
        for v in open_set:
            if n == None or g[v] + heuristic(v) < g[n] + heuristic(n):
                n = v

        # If goal node is reached or node has no neighbors
        if n == stop_node or Graph_nodes[n] == None:
            pass
        else:
            # Explore neighbors of current node
            for (m, weight) in get_neighbors(n):
                if m not in open_set and m not in closed_set:
                    open_set.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight
                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n
                        if m in closed_set:
                            closed_set.remove(m)
                            open_set.add(m)

        # If no path exists
        if n == None:
            print('Path does not exist!')
            return None

        # If goal node is found, reconstruct and return the path
        if n == stop_node:
            path = []
            while parents[n] != n:
                path.append(n)
                n = parents[n]
            path.append(start_node)
            path.reverse()
            print('Path found: {}'.format(path))
            return path

        open_set.remove(n)
        closed_set.add(n)

    print('Path does not exist!')
    return None

# Function to get neighbors of a node
def get_neighbors(v):
    if v in Graph_nodes:
        return Graph_nodes[v]
    else:
        return None

# Heuristic function (estimated cost from current node to goal node)
def heuristic(n):
    return H_dist[n]

# Function to get input from user
def get_input_from_user():
    num_edges = int(input("Enter the number of edges: "))  # Input number of edges
    # Input edges and distances between nodes
    for _ in range(num_edges):
        city1, city2, distance = input("Enter city1 city2 distance: ").split()
        distance = int(distance)
        if city1 not in Graph_nodes:
            Graph_nodes[city1] = []
        if city2 not in Graph_nodes:
            Graph_nodes[city2] = []
        Graph_nodes[city1].append((city2, distance))
        Graph_nodes[city2].append((city1, distance))

    # Input heuristic values for each node
    for node in Graph_nodes:
        heuristic_value = int(input(f"Enter heuristic value for node {node}: "))
        H_dist[node] = heuristic_value

Graph_nodes = {}  # Dictionary to store graph nodes and their neighbors
H_dist = {}  # Dictionary to store heuristic values for nodes

# Main function
if __name__ == "__main__":
    get_input_from_user()  # Get input from user
    start_node = input("Enter the start node: ")  # Input start node
    stop_node = input("Enter the destination node: ")  # Input destination node
    aStarAlgo(start_node, stop_node)  # Run A* algorithm
