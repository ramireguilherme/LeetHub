import heapq

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacency_list = {v: [] for v in range(vertices)}

    def add_edge(self, src, dest, weight):
        self.adjacency_list[src].append((dest, weight))
        self.adjacency_list[dest].append((src, weight))

    def dijkstra(self, source, target, max_weight):
        visited = [False] * self.vertices
        distance = [float('inf')] * self.vertices
        distance[source] = 0
        pq = [(0, source)]  # Priority queue (distance, node)

        while pq:
            dist, node = heapq.heappop(pq)
            if node == target:
                return True
            visited[node] = True
            for neighbor, weight in self.adjacency_list[node]:
                if not visited[neighbor] and weight <= max_weight:
                    if distance[node] + weight < distance[neighbor]:
                        distance[neighbor] = distance[node] + weight
                        heapq.heappush(pq, (distance[neighbor], neighbor))
        return False

def binary_search_dijkstra_minmax_path(graph, source, target):
    left = 0
    right = float('inf')

    while left < right:
        mid = left + (right - left) // 2
        if graph.dijkstra(source, target, mid):
            right = mid
        else:
            left = mid + 1

    return left


rows, cols = map(int, input().split())
source = 0 
target = rows * cols  
graph = Graph(target)
matrix = [list(map(int, input().split())) for _ in range(rows)]
for i in range(rows):
    for j in range(cols):
        if i < rows - 1:
            if -1*(matrix[i][j] - matrix[i + 1][j]) >= 0:
                graph.add_edge(i * cols + j, (i + 1) * cols + j, -1*(matrix[i][j] - matrix[i + 1][j]))
        if j < cols - 1:
            if -1*(matrix[i][j] - matrix[i][j + 1]) >= 0:
                graph.add_edge(i * cols + j, i * cols + j + 1, -1*(matrix[i][j] - matrix[i][j + 1]))
print(graph.adjacency_list)
min_max_weight = binary_search_dijkstra_minmax_path(graph, source, target)
print(min_max_weight)
print("The minimum maximum edge weight in the path is:", min_max_weight)
