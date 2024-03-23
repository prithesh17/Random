def bfs(graph, start, goal):
    visited = set()  # Set to keep track of visited nodes
    queue = [start]  # Queue to store nodes for BFS traversal
    while queue:
        node = queue.pop(0)  # Get the first node from the queue
        if node not in visited:
            print(node, end=' ')  # Print the node
            visited.add(node)  # Mark the node as visited
            if node == goal:  # Check if the goal node is reached
                break
            # Add unvisited neighbors of the current node to the queue
            queue.extend(neighbor for neighbor in graph[node] if neighbor not in visited)

def dfs(graph, node, visited, goal):
    if node not in visited:
        print(node, end=' ')  # Print the node
        visited.add(node)  # Mark the node as visited
        if node == goal:  # Check if the goal node is reached
            return
        # Recursively visit unvisited neighbors of the current node
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited, goal)

# Main function
graph = {}  # Dictionary to store the graph
nodes = int(input('Enter the number of city nodes in the graph: '))  # Get the number of nodes in the graph
for _ in range(nodes):
    node = input('Enter the city node name: ')  # Get the name of the node
    neighbors = input('Enter the neighbors of the city ' + node + ': ').split()  # Get the neighbors of the node
    graph[node] = set(neighbors)  # Add the node and its neighbors to the graph

# Breadth First Search (BFS)
start_node = input('Enter the source node for BFS: ')  # Get the source node for BFS
goal_node = input('Enter the goal node for BFS: ')  # Get the goal node for BFS
print("BFS:", end=" ")
bfs(graph, start_node, goal_node)  # Perform BFS traversal
print()

# Depth First Search (DFS)
start_node = input('Enter the source node for DFS: ')  # Get the source node for DFS
goal_node = input('Enter the goal node for DFS: ')  # Get the goal node for DFS
print("DFS:", end=" ")
dfs(graph, start_node, set(), goal_node)  # Perform DFS traversal
