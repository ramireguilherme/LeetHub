#include <iostream>
#include <vector>

int main() {
 
    int V = 0; // number of vertices
    std::vector<std::vector<int>> AdjList(V); // adjacency list representation

    // Your code here

    bool hasNegativeCycle = false;
    // after running the O(VE) Bellman Ford's algorithm
    for (int u = 0; u < V; u++) { // one more pass to check
        for (int j = 0; j < (int)AdjList[u].size(); j++) {
            int v = AdjList[u][j];
            if (dist[v.first] > dist[u] + v.second) { // if this is still possible
                hasNegativeCycle = true; // then negative cycle exists!
            }
        }
    }
    printf("Negative Cycle Exists? %s\n", hasNegativeCycle ? "Yes" : "No");

    return 0;
}