class Graph:
    def __init__(self, nodes):
        self.nodes = nodes
        pass        
    
    def bellman_ford(self, src):
        dist = [float('inf') for i in range(self.nodes)]
        dist[src] = 0
        for i in range(self.nodes-1):
            for u, v, w in self.edges:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
        return dist

nodes, edges , queries = map(int, input().split())
for i in range(edges):
    u, v , w = map(int, input().split())
