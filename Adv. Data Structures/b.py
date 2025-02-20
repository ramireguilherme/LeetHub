class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [1] * size

    def find(self, p):
        if self.parent[p] != p:
            self.parent[p] = self.find(self.parent[p])  # Path compression
        return self.parent[p]

    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)

        if rootP != rootQ:
            if self.rank[rootP] > self.rank[rootQ]:
                self.parent[rootQ] = rootP
            elif self.rank[rootP] < self.rank[rootQ]:
                self.parent[rootP] = rootQ
            else:
                self.parent[rootQ] = rootP
                self.rank[rootP] += 1

n , queries = map(int, input().split())
uf = UnionFind(n)
for _ in range(queries):
    query = input().split()
    if query[0] == '?':
        print('yes' if uf.find(int(query[1])) == uf.find(int(query[2])) else 'no')
    else:
        uf.union(int(query[1]), int(query[2]))

