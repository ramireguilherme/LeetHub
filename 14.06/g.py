import math

def can_reach(gopher, hole, max_distance):
    return math.dist(gopher, hole) <= max_distance

def bpm(u, match, seen, adj):
    for v in adj[u]:
        if not seen[v]:
            seen[v] = True
            if match[v] == -1 or bpm(match[v], match, seen, adj):
                match[v] = u
                return True
    return False

def max_bipartite_matching(adj, n, m):
    match = [-1] * m
    result = 0
    for i in range(n):
        seen = [False] * m
        if bpm(i, match, seen, adj):
            result += 1
    return result

while True:
    try:
        n ,m,s,v = map(int, input().split())   

        gophers = []
        for i in range(n):
            x ,y = map(float, input().split())            
            gophers.append((x, y))

        holes = []
        for i in range(m):
            x ,y = map(float, input().split())            
            holes.append((x, y))

        max_distance = s * v
        adj = [[] for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if can_reach(gophers[i], holes[j], max_distance):
                    adj[i].append(j)

        max_matching = max_bipartite_matching(adj, n, m)
        vulnerable_gophers = n - max_matching
        print(vulnerable_gophers)
    except EOFError:
        break