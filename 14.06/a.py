from collections import deque, defaultdict

def bfs(capacity, source, sink, parent):
    visited = set()
    queue = deque([source])
    visited.add(source)

    while queue:
        u = queue.popleft()

        for v in capacity[u]:
            if v not in visited and capacity[u][v] - flow[u][v] > 0:
                queue.append(v)
                visited.add(v)
                parent[v] = u
                if v == sink:
                    return True
    return False

def edmonds_karp(capacity, source, sink):
    global flow
    flow = defaultdict(lambda: defaultdict(int))
    parent = {}

    max_flow = 0

    while bfs(capacity, source, sink, parent):
        path_flow = float('Inf')
        s = sink

        while s != source:
            path_flow = min(path_flow, capacity[parent[s]][s] - flow[parent[s]][s])
            s = parent[s]

        max_flow += path_flow

        v = sink
        while v != source:
            u = parent[v]
            flow[u][v] += path_flow
            flow[v][u] -= path_flow
            v = parent[v]

    return max_flow

import sys
input = sys.stdin.read
data = input().splitlines()

network_number = 1
index = 0

while index < len(data):
    n = int(data[index])
    if n == 0:
        break

    index += 1
    s, t, c = map(int, data[index].split())
    index += 1

    capacity = defaultdict(lambda: defaultdict(int))

    for _ in range(c):
        u, v, bw = map(int, data[index].split())
        index += 1
        capacity[u][v] += bw
        capacity[v][u] += bw

    max_bandwidth = edmonds_karp(capacity, s, t)

    print(f"Network {network_number}")
    print(f"The bandwidth is {max_bandwidth}.")
    print()

    network_number += 1

