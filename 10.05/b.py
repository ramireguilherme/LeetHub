from collections import deque, defaultdict

def add_edge(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)

def bfs_count_nodes(adj, start, visited):
    queue = deque([start])
    visited[start] = True
    size = 0
    while queue:
        node = queue.popleft()
        size += 1  # Increment the size for each node visited
        for neighbor in adj[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
    return size

def component_sizes(n, adj):
    visited = [False] * n
    sizes = []
    for i in range(n):
        if not visited[i]:
            comp_size = bfs_count_nodes(adj, i, visited)
            sizes.append(comp_size)
    return sizes

vertices , n_edges = map(int, input().split())

edges = [(0, 1), (1, 2), (3, 4), (5, 6)]  # List of edges
adj = defaultdict(list)

for u, v in edges:
    add_edge(adj, u, v)

sizes = component_sizes(n, adj)
print("Sizes of connected components:", sizes)
