def bellman_ford(graph, V, source):
    dist = [float("inf")] * V
    dist[source] = 0
    
    for _ in range(V - 1):
        for u, v, w in graph: 
            if dist[u] != float("inf") and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    
    for u, v, w in graph:
        if dist[u] != float("inf") and dist[u] + w < dist[v]:
            print("possible")
            return True
    print("not possible")
    return False

tests = int(input())
for __ in range(tests):
    vertices, edges = map(int, input().split())
    V = vertices
    g = []

    for _ in range(edges):
        u,v,w = map(int, input().split())
        g.append((u, v, w))

    bellman_ford(g, V, 0)
    