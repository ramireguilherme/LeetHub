class Graph:
    def __init__(self):
        self.adj_list = {}
        self.visited = set()

    def add_edge(self, u, v):
        if u not in self.adj_list:
            self.adj_list[u] = []
        if v not in self.adj_list:
            self.adj_list[v] = []
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def __str__(self):
        output = ""
        for node, neighbors in self.adj_list.items():
            output += f"{node}: {', '.join(neighbors)}\n"
        return output
    
    def dfs(self, start):
        self.visited.add(start)
        for neighbor in self.adj_list[start]:
            if neighbor not in self.visited:
                self.dfs(neighbor)
                
tests = int(input())
for __ in range(tests):
    g = Graph()
    while True:
        line = input()
        if '*' in line:
            break
        u = line[1]
        v = line[3]
        g.add_edge(u, v)
    vertices_list = input().split(',')
    trees , acorns = 0, 0
    for vertex in vertices_list:
        if vertex not in g.adj_list:
            acorns += 1
        elif vertex not in g.visited:
            g.dfs(vertex)
            trees += 1
    print(f'There are {trees} tree(s) and {acorns} acorn(s).')
