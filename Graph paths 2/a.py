import heapq

def dijkstra(graph, start):
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    queue = [(0, start)]

    while queue:
        current_distance, current_vertex = heapq.heappop(queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return distances

tests = int(input())
for i in range(tests):
    vertices, edges, start, end = map(int, input().split())
    graph = {vertex: {} for vertex in range(vertices)}

    for j in range(edges):
        u, v, weight = map(int, input().split())


        graph[u][v] = weight
        graph[v][u] = weight

    distances = dijkstra(graph, start)
    print("Case #{}:".format(i+1), end=" ")
    print(distances[end] if distances[end] != float('inf') else "unreachable")