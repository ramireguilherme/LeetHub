from collections import deque, defaultdict

def add_edge(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)

def bfs(adj, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        node = queue.popleft()
        for neighbor in adj[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

def count_components(n, adj):
    visited = [False] * n
    component_count = 0
    for i in range(n):
        if not visited[i]:
            bfs(adj, i, visited)
            component_count += 1
    return component_count

def min_edges_to_connect(n, adj):
    components = count_components(n, adj)
    return components - 1 if components > 1 else 0

tests = int(input())

for __ in range(tests):
    n =  int(input())
    n_edges = int(input())
    edges = []
    for _ in range(n_edges):
        u, v = map(int, input().split())
        edges.append((u, v))
    adj = defaultdict(list)

    for u, v in edges:
        add_edge(adj, u, v)

    print(min_edges_to_connect(n, adj))
