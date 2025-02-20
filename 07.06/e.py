class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

def kruskal_minmax_path(n, edges, source, target):
    edges.sort(key=lambda x: x[2])  # Sort edges by weight
    ds = DisjointSet(n)
    mst = []

    for u, v, weight in edges:
        if ds.find(u) != ds.find(v):
            ds.union(u, v)
            mst.append((u, v, weight))
            if ds.find(source) == ds.find(target):
                break

    adj_list = [[] for _ in range(n)]
    for u, v, weight in mst:
        adj_list[u].append((v, weight))
        adj_list[v].append((u, weight))

    def dfs(node, target, visited):
        if node == target:
            return 0
        visited[node] = True
        for neighbor, weight in adj_list[node]:
            if not visited[neighbor]:
                result = dfs(neighbor, target, visited)
                if result != -1:
                    return max(weight, result)
        return -1

    visited = [False] * n
    return dfs(source, target, visited)



test = 1
vertices, edges, queries = map(int, input().split())
while vertices != 0 and edges != 0 and queries != 0:
    edges_list = []
    for __ in range(edges):
        u,v,w = map(int, input().split())
        edges_list.append((u,v,w))
    print("Case #{}:".format(test))
    test += 1
    for __ in range(queries):
        source, target = map(int, input().split())
        value = kruskal_minmax_path(vertices+1, edges_list, source, target)
        print(value if value != -1 else "no path")
    print()
    vertices, edges, queries = map(int, input().split())