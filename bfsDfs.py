import collections

def bfs(graph, source, destination):
    visited = set()
    queue = collections.deque([(source, [source])])
    
    while queue:
        node, path = queue.popleft()
        if node == destination:
            return path
        visited.add(node)
        for neighbour in graph[node]:
            if neighbour not in visited:
                queue.append((neighbour, path + [neighbour]))

    return None

def dfs(graph, node, destination, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = [node]

    visited.add(node)

    if node == destination:
        return path

    for neighbour in graph[node]:
        if neighbour not in visited:
            new_path = dfs(graph, neighbour, destination, visited, path + [neighbour])
            if new_path:
                return new_path

    return None

def add_edge(graph, u, v):
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append(v)
    graph[v].append(u)

graph = {}
n = int(input("Enter the number of edges: "))
print("Enter the edges (format: node1 node2):")
for _ in range(n):
    edge = input().split()
    u, v = map(int, edge)
    add_edge(graph, u, v)

source = int(input("Enter the source node: "))
destination = int(input("Enter the destination node: "))

bfs_path = bfs(graph, source, destination)
dfs_path = dfs(graph, source, destination)

print("BFS Path:", bfs_path)
print("DFS Path:", dfs_path)





