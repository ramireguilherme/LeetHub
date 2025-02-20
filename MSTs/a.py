import math
from itertools import combinations

class UnionFind:
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

def calculate_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def kruskal_mst(points):
    edges = []
    n = len(points)
    
    for (i, j) in combinations(range(n), 2):
        distance = calculate_distance(points[i], points[j])
        edges.append((distance, i, j))
    
    edges.sort()
    
    uf = UnionFind(n)
    mst = []
    
    for distance, u, v in edges:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst.append((u, v, distance))
    
    return mst

tests = int(input())
for __ in range(tests):
    points = []
    vertices = int(input())
    points = [(float(x), float(y)) for _ in range(vertices) for x, y in [input().split()]]
    mst = kruskal_mst(points)
    print("{:.3f}".format(sum(distance for u, v, distance in mst)))
