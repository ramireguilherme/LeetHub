class Graph:
    def __init__(self):
        self.graph = {}  
    
    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def dfs(self, start):
        visited = set()  

        def dfs_visit(vertex):
            if vertex in visited:
                return vertex
            visited.add(vertex)
            for neighbor in self.graph[vertex]:
                if dfs_visit(neighbor):
                    return True
            return False
        
        dfs_visit(start)

g = Graph()
n = int(input())
traverse = list(map(int, input().split()))
for i in range(n):
    g.add_edge(i+1, traverse[i])
v = []
for i in range(1, n+1):
    visited = g.dfs(i)
    v.append(visited)
print(v)