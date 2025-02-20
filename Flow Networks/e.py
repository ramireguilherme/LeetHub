from collections import deque, defaultdict


# BFS function to find path with available capacity
def bfs_capacity(graph, source, sink, parent):
    visited = set()
    queue = deque([source])
    visited.add(source)
    
    while queue:
        u = queue.popleft()
        
        for v in graph[u]:
            if v not in visited and graph[u][v] > 0:
                queue.append(v)
                visited.add(v)
                parent[v] = u
                if v == sink:
                    return True
    return False

# Ford-Fulkerson method to calculate maximum flow
def ford_fulkerson(graph, source, sink):
    parent = [-1] * len(graph)
    max_flow = 0
    
    while bfs_capacity(graph, source, sink, parent):
        path_flow = float('Inf')
        s = sink
        
        while s != source:
            path_flow = min(path_flow, graph[parent[s]][s])
            s = parent[s]
        
        max_flow += path_flow
        v = sink
        
        while v != source:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = parent[v]
    
    return max_flow

vertices , edges , source , sink = map(int, input().split())

capacity = defaultdict(lambda: defaultdict(int))

for _ in range(edges):
    u, v, bw = map(int, input().split())
    capacity[u][v] += bw
    capacity[v][u] += bw

max_flow = ford_fulkerson(capacity, source, sink)
solution_edges = []
for u in range(vertices):
    for v in capacity[u]:
        if capacity[u][v] <= 0:
            flow = -capacity[u][v]
            solution_edges.append((u, v, flow))
print(f'{vertices} {max_flow} {len(solution_edges)}')
for u, v, f in solution_edges:
    print(u, v, f)